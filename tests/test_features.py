from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from metro_perceptron.features import build_feature_vector


class TestFeatures(unittest.TestCase):
    def test_build_feature_vector_runtime(self) -> None:
        row = build_feature_vector(2.0, 40.0, 1.0)
        self.assertEqual(len(row), 4)
        self.assertEqual(row[0], 2.0)
        self.assertEqual(row[1], 40.0)
        self.assertEqual(row[2], 1.0)
        self.assertAlmostEqual(row[3], 3.0, places=9)


if __name__ == "__main__":
    unittest.main()
