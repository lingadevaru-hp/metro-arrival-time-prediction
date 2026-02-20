from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List

from .data import MetroStop
from .features import build_feature_vector
from .model import PerceptronRegressor


@dataclass(frozen=True)
class ScheduleRow:
    station_order: int
    station_name: str
    predicted_segment_min: float
    arrival_time: str
    departure_time: str


def predict_arrival_schedule(
    stops: List[MetroStop],
    model: PerceptronRegressor,
    starting_departure_time: str,
    time_format: str = "%H:%M",
) -> List[ScheduleRow]:
    if not stops:
        return []

    current_arrival = datetime.strptime(starting_departure_time, time_format)
    rows: List[ScheduleRow] = []

    first = stops[0]
    rows.append(
        ScheduleRow(
            station_order=first.station_order,
            station_name=first.station_name,
            predicted_segment_min=0.0,
            arrival_time=current_arrival.strftime(time_format),
            departure_time=current_arrival.strftime(time_format),
        )
    )

    for idx in range(1, len(stops)):
        stop = stops[idx]
        prev_stop = stops[idx - 1]
        prev_dwell = 0.0 if idx == 1 else prev_stop.dwell_time_min
        features = build_feature_vector(
            distance_from_prev_km=stop.distance_from_prev_km,
            avg_speed_kmph=stop.avg_speed_kmph,
            prev_station_dwell_min=prev_dwell,
        )
        segment_time = max(0.0, model.predict_one(features))
        current_arrival = current_arrival + timedelta(minutes=segment_time)
        departure_time = current_arrival + timedelta(minutes=stop.dwell_time_min)

        rows.append(
            ScheduleRow(
                station_order=stop.station_order,
                station_name=stop.station_name,
                predicted_segment_min=round(segment_time, 3),
                arrival_time=current_arrival.strftime(time_format),
                departure_time=departure_time.strftime(time_format),
            )
        )
    return rows
