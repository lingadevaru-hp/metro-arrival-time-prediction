# Metro Arrival Time Prediction (Perceptron-Based)

This project predicts metro train arrival times at each station using a single-layer perceptron-style linear regressor.

It covers all internship roles:
- ML model logic
- architecture design
- dataset/database
- implementation
- UI/documentation
- testing/validation

## Problem Inputs

- Starting departure time
- Distance between stations
- Average train speed
- Dwell time at stations

## Project Structure

```text
data/
  metro_line.csv
docs/
  architecture.md
  member_work_guide.md
scripts/
  run_demo.py
src/metro_perceptron/
  __init__.py
  data.py
  features.py
  model.py
  scheduler.py
  evaluation.py
tests/
  conftest.py
  test_features.py
  test_model.py
  test_pipeline.py
ui/
  streamlit_app.py
```

## Quick Start

1. Run demo pipeline:

```bash
python scripts/run_demo.py --departure 08:30
```

2. Run tests:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

3. Optional UI:

```bash
streamlit run ui/streamlit_app.py
```

## Notes

- The model is a perceptron-style linear neuron trained with gradient descent on regression loss.
- Target value is segment travel time (minutes) from previous station to current station.
- Predicted station arrivals are accumulated from the starting departure time.
