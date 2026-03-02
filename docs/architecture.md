# Architecture Design

## 1. High-Level Flow

1. Read station dataset from CSV.
2. Persist dataset into SQLite for structured querying and reproducibility.
3. Build segment-level training features:
   - distance from previous station
   - average speed
   - previous station dwell time
   - derived runtime feature `(distance / speed) * 60`
4. Train perceptron-style linear regressor.
5. Predict each segment time and accumulate arrival times from starting departure.
6. Serve outputs through CLI, optional UI, and tests.

## 2. Component Diagram

```text
CSV Dataset -> Data Layer -> Feature Engineering -> Perceptron Model -> Scheduler -> Outputs
     |             |                |                    |               |
     |             |                |                    |               +--> CLI / UI table
     |             |                |                    +--> Validation metrics
     |             +--> SQLite DB   +--> X, y matrix
```

## 3. Files by Layer

- Data Layer: `src/metro_perceptron/data.py`, `data/metro_line.csv`
- Feature Layer: `src/metro_perceptron/features.py`
- Model Layer: `src/metro_perceptron/model.py`
- Scheduling Layer: `src/metro_perceptron/scheduler.py`
- Validation Layer: `src/metro_perceptron/evaluation.py`, `tests/`
- Interface Layer: `scripts/run_demo.py`, `ui/streamlit_app.py`

## 4. Why Perceptron for This Use Case

- A single-layer perceptron (linear neuron) is lightweight and interpretable.
- It is suitable for quick schedule estimation when relationships are approximately linear after feature engineering.
- This project demonstrates practical application of linear models in transportation operations.
