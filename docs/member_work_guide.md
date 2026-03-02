# Internship Member-Wise Work Guide (Completed)

This document maps all 6 member responsibilities to completed deliverables in this project.

## Member 1 - ML Model Logic Building

Completed:
- Defined target: segment arrival time prediction in minutes.
- Designed perceptron-style linear regressor training logic.
- Added feature scaling, gradient descent, L2 regularization, and convergence check.

Files:
- `src/metro_perceptron/model.py`
- `src/metro_perceptron/features.py`

## Gare Nagaraju - Architecture Design

Completed:
- Designed end-to-end modular architecture (data -> features -> model -> scheduler -> interfaces).
- Documented component interaction and rationale.

Files:
- `docs/architecture.md`
- `README.md`

## Member 3 - Dataset / Database

Completed:
- Created realistic metro line dataset with station order, distance, speed, dwell, and observed time.
- Implemented CSV loader and SQLite persistence/query layer.

Files:
- `data/metro_line.csv`
- `src/metro_perceptron/data.py`

## Achyuth - Model Implementation

Completed:
- Implemented training/inference pipeline.
- Implemented schedule prediction from starting departure time.
- Added runnable demo script that trains model and prints schedule.

Files:
- `src/metro_perceptron/model.py`
- `src/metro_perceptron/scheduler.py`
- `scripts/run_demo.py`

## Khushi - UI & Documentation

Completed:
- Built optional Streamlit UI for model controls and schedule visualization.
- Wrote project README and architecture documentation.

Files:
- `ui/streamlit_app.py`
- `README.md`
- `docs/architecture.md`

## Member 6 - Testing & Validation

Completed:
- Added unit tests for feature creation, model fit quality, and schedule monotonicity.
- Added MAE/RMSE/R2 metrics.

Files:
- `tests/test_features.py`
- `tests/test_model.py`
- `tests/test_pipeline.py`
- `src/metro_perceptron/evaluation.py`

## Deliverables Checklist

- [x] Starting departure time handled
- [x] Distance between stations handled
- [x] Average speed handled
- [x] Dwell time handled
- [x] Linear model application explained and demonstrated
- [x] Full 6-member work completed in one integrated project
