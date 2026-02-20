# Achyuth - Model Implementation

## Role Summary
You are responsible for integrating data, training, prediction, and schedule generation into a working pipeline.

## Implementation Scope
- Train the perceptron regressor on segment-level data.
- Predict segment travel times.
- Accumulate station arrival times from a starting departure time.
- Print final schedule through a runnable script.

## Your Owned Files (Show These)
- `scripts/run_demo.py`
- `src/metro_perceptron/scheduler.py`
- `src/metro_perceptron/model.py`

## What You Should Explain in Review
1. The first station uses the user-provided start departure time.
2. Each next station time is previous arrival plus predicted segment minutes.
3. Dwell time is added for station departure output.
4. Negative predictions are clamped at zero for safe scheduling output.

## Exact Speaking Script
"My responsibility was turning the ML logic into a complete executable pipeline. The demo script loads data, trains the model, computes evaluation metrics, and generates station-wise arrival and departure times from a user-given start time. The scheduler accumulates segment predictions to create a practical metro timetable."

## Demo Points
- Run: `python scripts/run_demo.py --departure 08:30`
- Open `src/metro_perceptron/scheduler.py` and explain `predict_arrival_schedule(...)`.

## Likely Questions and Answers
Q: How does user input affect output?
A: Changing starting departure shifts the full predicted schedule timeline.

Q: What if model predicts invalid negative minutes?
A: We clamp segment time to `max(0, prediction)` for robustness.
