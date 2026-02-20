from __future__ import annotations

from typing import List, Tuple

from .data import MetroStop


def build_feature_vector(
    distance_from_prev_km: float,
    avg_speed_kmph: float,
    prev_station_dwell_min: float,
) -> List[float]:
    if avg_speed_kmph <= 0:
        run_time_min = 0.0
    else:
        run_time_min = (distance_from_prev_km / avg_speed_kmph) * 60.0
    return [
        distance_from_prev_km,
        avg_speed_kmph,
        prev_station_dwell_min,
        run_time_min,
    ]


def build_training_data(stops: List[MetroStop]) -> Tuple[List[List[float]], List[float]]:
    if len(stops) < 2:
        return [], []

    x_data: List[List[float]] = []
    y_data: List[float] = []
    for idx in range(1, len(stops)):
        stop = stops[idx]
        prev_stop = stops[idx - 1]
        features = build_feature_vector(
            distance_from_prev_km=stop.distance_from_prev_km,
            avg_speed_kmph=stop.avg_speed_kmph,
            prev_station_dwell_min=prev_stop.dwell_time_min,
        )
        x_data.append(features)
        y_data.append(stop.observed_segment_time_min)
    return x_data, y_data
