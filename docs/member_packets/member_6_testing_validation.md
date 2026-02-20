# Member 6 - Testing & Validation

## Role Summary
You are responsible for proving correctness and reliability of the solution.

## Validation Scope
- Unit tests for feature engineering
- Unit tests for model fitting behavior
- End-to-end pipeline tests for schedule generation
- Metric-based performance reporting

Metrics used:
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R2 (Coefficient of Determination)

## Your Owned Files (Show These)
- `tests/test_features.py`
- `tests/test_model.py`
- `tests/test_pipeline.py`
- `src/metro_perceptron/evaluation.py`

## What You Should Explain in Review
1. Tests verify each critical stage independently.
2. Pipeline test validates integration of data -> model -> schedule.
3. Time sequence is checked to ensure no backward arrival order.
4. Metrics confirm prediction quality numerically.

## Exact Speaking Script
"My role was testing and validation. I wrote unit tests for features, model, and full pipeline integration. I also implemented MAE, RMSE, and R2 to quantify model quality. The current results show high fit quality and a valid increasing arrival timeline, confirming that the system is both correct and reliable."

## Demo Points
- Run: `python -m unittest discover -s tests -p "test_*.py" -v`
- Show metrics output from `python scripts/run_demo.py --departure 08:30`.

## Likely Questions and Answers
Q: Why test both unit and end-to-end?
A: Unit tests catch local defects; end-to-end test validates system integration.

Q: Which metric is most important here?
A: MAE is directly interpretable in minutes, so it is practical for operations.
