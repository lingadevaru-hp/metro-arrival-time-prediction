from __future__ import annotations

from pathlib import Path
import sys

import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from metro_perceptron.data import load_stops_from_csv
from metro_perceptron.evaluation import mae, r2_score, rmse
from metro_perceptron.features import build_training_data
from metro_perceptron.model import PerceptronRegressor
from metro_perceptron.scheduler import predict_arrival_schedule


def main() -> None:
    st.set_page_config(page_title="Metro Arrival Predictor", page_icon="M", layout="wide")
    st.title("Metro Train Arrival Time Predictor")
    st.caption("Perceptron-based linear regression for station-by-station arrival estimation")

    csv_path = ROOT / "data" / "metro_line.csv"
    stops = load_stops_from_csv(csv_path)
    x_data, y_data = build_training_data(stops)

    col1, col2, col3 = st.columns(3)
    with col1:
        learning_rate = st.slider("Learning Rate", 0.001, 0.1, 0.01, 0.001)
    with col2:
        epochs = st.slider("Epochs", 200, 5000, 3000, 200)
    with col3:
        departure = st.text_input("Starting Departure (HH:MM)", value="08:30")

    model = PerceptronRegressor(learning_rate=learning_rate, epochs=epochs, l2=0.0001)
    model.fit(x_data, y_data)
    y_pred = model.predict(x_data)

    m1, m2, m3 = st.columns(3)
    m1.metric("MAE", f"{mae(y_data, y_pred):.3f}")
    m2.metric("RMSE", f"{rmse(y_data, y_pred):.3f}")
    m3.metric("R2", f"{r2_score(y_data, y_pred):.3f}")

    schedule = predict_arrival_schedule(stops, model, departure)
    st.subheader("Predicted Station Schedule")
    st.table(
        [
            {
                "Order": row.station_order,
                "Station": row.station_name,
                "Segment Minutes": row.predicted_segment_min,
                "Arrival": row.arrival_time,
                "Departure": row.departure_time,
            }
            for row in schedule
        ]
    )


if __name__ == "__main__":
    main()
