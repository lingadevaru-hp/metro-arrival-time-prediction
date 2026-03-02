from __future__ import annotations

import csv
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass(frozen=True)
class MetroStop:
    line_name: str
    station_order: int
    station_name: str
    distance_from_prev_km: float
    avg_speed_kmph: float
    dwell_time_min: float
    observed_segment_time_min: float


def _to_stop(row: dict) -> MetroStop:
    return MetroStop(
        line_name=row["line_name"],
        station_order=int(row["station_order"]),
        station_name=row["station_name"],
        distance_from_prev_km=float(row["distance_from_prev_km"]),
        avg_speed_kmph=float(row["avg_speed_kmph"]),
        dwell_time_min=float(row["dwell_time_min"]),
        observed_segment_time_min=float(row["observed_segment_time_min"]),
    )


def load_stops_from_csv(csv_path: str | Path) -> List[MetroStop]:
    path = Path(csv_path)
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        stops = [_to_stop(row) for row in reader]
    stops.sort(key=lambda s: s.station_order)
    return stops


def write_csv_to_sqlite(csv_path: str | Path, db_path: str | Path) -> None:
    stops = load_stops_from_csv(csv_path)
    conn = sqlite3.connect(str(db_path))
    try:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS metro_stops (
                line_name TEXT NOT NULL,
                station_order INTEGER NOT NULL,
                station_name TEXT NOT NULL,
                distance_from_prev_km REAL NOT NULL,
                avg_speed_kmph REAL NOT NULL,
                dwell_time_min REAL NOT NULL,
                observed_segment_time_min REAL NOT NULL,
                PRIMARY KEY (line_name, station_order)
            )
            """
        )
        cur.execute("DELETE FROM metro_stops")
        cur.executemany(
            """
            INSERT INTO metro_stops (
                line_name,
                station_order,
                station_name,
                distance_from_prev_km,
                avg_speed_kmph,
                dwell_time_min,
                observed_segment_time_min
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            [
                (
                    s.line_name,
                    s.station_order,
                    s.station_name,
                    s.distance_from_prev_km,
                    s.avg_speed_kmph,
                    s.dwell_time_min,
                    s.observed_segment_time_min,
                )
                for s in stops
            ],
        )
        conn.commit()
    finally:
        conn.close()


def load_stops_from_db(db_path: str | Path, line_name: str) -> List[MetroStop]:
    conn = sqlite3.connect(str(db_path))
    try:
        cur = conn.cursor()
        rows = cur.execute(
            """
            SELECT
                line_name,
                station_order,
                station_name,
                distance_from_prev_km,
                avg_speed_kmph,
                dwell_time_min,
                observed_segment_time_min
            FROM metro_stops
            WHERE line_name = ?
            ORDER BY station_order ASC
            """,
            (line_name,),
        ).fetchall()
    finally:
        conn.close()

    return [
        MetroStop(
            line_name=r[0],
            station_order=int(r[1]),
            station_name=r[2],
            distance_from_prev_km=float(r[3]),
            avg_speed_kmph=float(r[4]),
            dwell_time_min=float(r[5]),
            observed_segment_time_min=float(r[6]),
        )
        for r in rows
    ]
