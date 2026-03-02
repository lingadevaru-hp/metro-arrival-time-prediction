from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from metro_perceptron.data import load_stops_from_csv
from metro_perceptron.evaluation import mae, r2_score
from metro_perceptron.features import build_training_data
from metro_perceptron.model import PerceptronRegressor
from metro_perceptron.scheduler import predict_arrival_schedule


class TestPipeline(unittest.TestCase):
    def test_end_to_end_pipeline(self) -> None:
        csv_path = ROOT / "data" / "metro_line.csv"
        stops = load_stops_from_csv(csv_path)

        x_data, y_data = build_training_data(stops)
        model = PerceptronRegressor(learning_rate=0.01, epochs=4000, l2=0.0001)
        model.fit(x_data, y_data)

        preds = model.predict(x_data)
        self.assertLess(mae(y_data, preds), 0.5)
        self.assertGreater(r2_score(y_data, preds), 0.8)

        schedule = predict_arrival_schedule(stops, model, "08:30")
        self.assertEqual(len(schedule), len(stops))
        self.assertEqual(schedule[0].arrival_time, "08:30")

        times = [row.arrival_time for row in schedule]
        self.assertEqual(times, sorted(times))


if __name__ == "__main__":
    unittest.main()
