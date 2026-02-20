from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from metro_perceptron.data import load_stops_from_csv, write_csv_to_sqlite
from metro_perceptron.evaluation import mae, r2_score, rmse
from metro_perceptron.features import build_training_data
from metro_perceptron.model import PerceptronRegressor
from metro_perceptron.scheduler import predict_arrival_schedule


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Train perceptron model and predict metro arrival schedule."
    )
    parser.add_argument(
        "--csv",
        default=str(ROOT / "data" / "metro_line.csv"),
        help="Path to metro CSV dataset",
    )
    parser.add_argument(
        "--db",
        default=str(ROOT / "data" / "metro_line.db"),
        help="Path to SQLite database output",
    )
    parser.add_argument(
        "--departure",
        default="08:30",
        help="Starting departure time at first station (HH:MM)",
    )
    args = parser.parse_args()

    stops = load_stops_from_csv(args.csv)
    write_csv_to_sqlite(args.csv, args.db)

    x_data, y_data = build_training_data(stops)
    model = PerceptronRegressor(learning_rate=0.01, epochs=3000, l2=0.0001)
    model.fit(x_data, y_data)

    y_pred = model.predict(x_data)
    print("Model Validation")
    print(f"MAE : {mae(y_data, y_pred):.4f}")
    print(f"RMSE: {rmse(y_data, y_pred):.4f}")
    print(f"R2  : {r2_score(y_data, y_pred):.4f}")
    print()

    print(f"Predicted Schedule (start departure: {args.departure})")
    schedule = predict_arrival_schedule(stops, model, args.departure)
    for row in schedule:
        print(
            f"{row.station_order:02d} {row.station_name:<15} "
            f"segment={row.predicted_segment_min:>5.2f} min  "
            f"arrival={row.arrival_time}  depart={row.departure_time}"
        )


if __name__ == "__main__":
    main()
