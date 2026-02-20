# Member-Wise Explanation Notes (Presentation Helper)

Use this as a quick script during project explanation.

## Member 1 - ML Model Logic Building

What to explain:
- We framed the problem as segment travel-time prediction (previous station to current station).
- Inputs used: distance, average speed, previous station dwell time, and derived runtime `(distance/speed)*60`.
- We used a perceptron-style linear regressor with gradient descent.

How to justify:
- Linear relationship is practical for first-level metro scheduling.
- Model is interpretable and fast for operational use.

Show file:
- `src/metro_perceptron/model.py`
- `src/metro_perceptron/features.py`

## Member 2 (Gare Nagaraju) - Architecture Design

What to explain:
- Pipeline: Data -> Features -> Model -> Scheduler -> Outputs (CLI/UI/tests).
- Each layer is modular and independent, so future upgrades are easy.

How to justify:
- Separation of concerns improves maintainability and team collaboration.

Show file:
- `docs/architecture.md`

## Member 3 - Dataset / Database

What to explain:
- We created a station-wise dataset including order, distance, speed, dwell, observed segment time.
- Dataset can be loaded from CSV and stored in SQLite for structured querying.

How to justify:
- CSV is easy for editing; SQLite gives persistent and queryable storage.

Show file:
- `data/metro_line.csv`
- `src/metro_perceptron/data.py`

## Member 4 (Achyuth) - Model Implementation

What to explain:
- Trained model on segment-level data.
- Predicted each segment time and accumulated arrival times from starting departure time.
- Produced station-by-station arrival/departure schedule.

How to justify:
- Matches the real transit flow: departure at origin, travel segment, arrive, dwell, continue.

Show file:
- `scripts/run_demo.py`
- `src/metro_perceptron/scheduler.py`

## Member 5 (Khushi) - UI & Documentation

What to explain:
- Added Streamlit UI to adjust hyperparameters and starting time.
- Displayed metrics and final schedule table for easy stakeholder review.
- Added README and architecture docs for onboarding and reproducibility.

How to justify:
- Makes model understandable for non-technical users.

Show file:
- `ui/streamlit_app.py`
- `README.md`

## Member 6 - Testing & Validation

What to explain:
- Added unit tests for features, model fitting, and full pipeline.
- Evaluated with MAE, RMSE, and R2.
- Confirmed schedule timeline remains ordered.

How to justify:
- Tests prevent regressions; metrics prove model quality.

Show file:
- `tests/test_features.py`
- `tests/test_model.py`
- `tests/test_pipeline.py`
- `src/metro_perceptron/evaluation.py`

## 1-Minute Team Closing Script

- Problem: predict metro arrival times using operational inputs.
- Approach: perceptron-based linear model with engineered travel features.
- Output: accurate arrival schedule from a given starting departure time.
- Quality checks: unit tests + MAE/RMSE/R2 validation.
- Result: end-to-end working system covering logic, architecture, data, implementation, UI, and testing.
