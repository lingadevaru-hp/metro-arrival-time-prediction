from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List


def _dot(a: List[float], b: List[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


@dataclass
class PerceptronRegressor:
    learning_rate: float = 0.01
    epochs: int = 2000
    l2: float = 0.0
    tolerance: float = 1e-8
    weights: List[float] = field(default_factory=list)
    bias: float = 0.0
    feature_means: List[float] = field(default_factory=list)
    feature_stds: List[float] = field(default_factory=list)
    loss_history: List[float] = field(default_factory=list)

    def _compute_scaling(self, x_data: List[List[float]]) -> None:
        n_features = len(x_data[0])
        means = []
        stds = []
        for col in range(n_features):
            values = [row[col] for row in x_data]
            mean = sum(values) / len(values)
            var = sum((v - mean) ** 2 for v in values) / len(values)
            std = var**0.5
            if std == 0:
                std = 1.0
            means.append(mean)
            stds.append(std)
        self.feature_means = means
        self.feature_stds = stds

    def _scale(self, row: List[float]) -> List[float]:
        return [
            (value - mean) / std
            for value, mean, std in zip(row, self.feature_means, self.feature_stds)
        ]

    def fit(self, x_data: List[List[float]], y_data: List[float]) -> "PerceptronRegressor":
        if not x_data:
            raise ValueError("x_data is empty")
        if len(x_data) != len(y_data):
            raise ValueError("x_data and y_data length mismatch")

        self._compute_scaling(x_data)
        x_scaled = [self._scale(row) for row in x_data]
        n_features = len(x_scaled[0])

        self.weights = [0.0 for _ in range(n_features)]
        self.bias = 0.0
        self.loss_history = []

        previous_loss = float("inf")
        for _ in range(self.epochs):
            total_loss = 0.0
            for row, target in zip(x_scaled, y_data):
                prediction = _dot(self.weights, row) + self.bias
                error = prediction - target
                total_loss += error**2

                for j in range(n_features):
                    grad = (2.0 * error * row[j]) + (2.0 * self.l2 * self.weights[j])
                    self.weights[j] -= self.learning_rate * grad
                self.bias -= self.learning_rate * (2.0 * error)

            loss = total_loss / len(x_scaled)
            self.loss_history.append(loss)
            if abs(previous_loss - loss) < self.tolerance:
                break
            previous_loss = loss
        return self

    def predict_one(self, row: List[float]) -> float:
        if not self.weights:
            raise ValueError("Model is not trained")
        scaled = self._scale(row)
        return _dot(self.weights, scaled) + self.bias

    def predict(self, x_data: Iterable[List[float]]) -> List[float]:
        return [self.predict_one(row) for row in x_data]
