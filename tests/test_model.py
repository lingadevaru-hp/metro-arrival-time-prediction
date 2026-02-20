from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from metro_perceptron.model import PerceptronRegressor


class TestModel(unittest.TestCase):
    def test_model_fits_simple_linear_pattern(self) -> None:
        x_data = [
            [1.0, 10.0, 0.5, 2.0],
            [2.0, 20.0, 0.7, 3.0],
            [3.0, 30.0, 1.0, 4.0],
            [4.0, 40.0, 1.2, 5.0],
            [5.0, 50.0, 1.5, 6.0],
        ]
        y_data = [1.2 * row[0] + 0.8 * row[2] + 0.5 * row[3] + 0.1 for row in x_data]

        model = PerceptronRegressor(learning_rate=0.01, epochs=5000, l2=0.0001)
        model.fit(x_data, y_data)
        preds = model.predict(x_data)
        mean_abs_error = sum(abs(a - b) for a, b in zip(y_data, preds)) / len(y_data)
        self.assertLess(mean_abs_error, 0.05)


if __name__ == "__main__":
    unittest.main()
