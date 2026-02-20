from __future__ import annotations

from typing import Iterable, List


def mae(y_true: Iterable[float], y_pred: Iterable[float]) -> float:
    y_t = list(y_true)
    y_p = list(y_pred)
    if len(y_t) != len(y_p):
        raise ValueError("Length mismatch")
    return sum(abs(a - b) for a, b in zip(y_t, y_p)) / len(y_t)


def rmse(y_true: Iterable[float], y_pred: Iterable[float]) -> float:
    y_t = list(y_true)
    y_p = list(y_pred)
    if len(y_t) != len(y_p):
        raise ValueError("Length mismatch")
    mse = sum((a - b) ** 2 for a, b in zip(y_t, y_p)) / len(y_t)
    return mse**0.5


def r2_score(y_true: List[float], y_pred: List[float]) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("Length mismatch")
    mean_true = sum(y_true) / len(y_true)
    ss_res = sum((a - b) ** 2 for a, b in zip(y_true, y_pred))
    ss_tot = sum((a - mean_true) ** 2 for a in y_true)
    if ss_tot == 0:
        return 1.0
    return 1.0 - (ss_res / ss_tot)
