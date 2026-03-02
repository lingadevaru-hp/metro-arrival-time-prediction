# Lingadevaru - Testing & Validation

## What You Actually Built
- Created unit tests for feature generation correctness.
- Created model-fit test to verify learning behavior on known linear data.
- Created end-to-end pipeline test for integration correctness.
- Added numeric evaluation metrics for objective quality reporting.

## Validation Strategy You Should Explain
Three validation levels:
- Unit validation: each component works in isolation.
- Integration validation: all components work together.
- Metric validation: predictions are quantitatively acceptable.

Metrics:
- MAE: average absolute error in minutes.
- RMSE: penalizes larger errors strongly.
- R2: goodness of fit compared to baseline mean predictor.

## Files You Own (Show in Presentation)
- `tests/test_features.py`
- `tests/test_model.py`
- `tests/test_pipeline.py`
- `src/metro_perceptron/evaluation.py`

## 2-Minute Speaking Script (Ready to Read)
"I handled testing and validation. I built tests at multiple levels to ensure reliability.  
First, unit tests check that feature engineering and model learning logic are correct. Second, an end-to-end pipeline test confirms that data loading, training, prediction, and schedule generation all work together.  
I also added MAE, RMSE, and R2 so model quality is measured numerically instead of by visual inspection only.  
This gives confidence that the project is not only functional in demo mode but also technically reliable and regression-safe."

## What to Show on Screen (Order)
1. Run `python -m unittest discover -s tests -p "test_*.py" -v`.
2. Show all tests passing.
3. Open `tests/test_pipeline.py` and show timeline-order assertion.
4. Run `python scripts/run_demo.py --departure 08:30`.
5. Explain MAE, RMSE, and R2 values from output.

## Key Points If Panel Asks “What Exactly Did You Do?”
- I designed and implemented the full test strategy.
- I verified both logic correctness and integration correctness.
- I defined quantitative acceptance indicators.
- I ensured the schedule output is time-ordered and valid.

## Likely Viva Questions
Q: Why use both MAE and RMSE?
A: MAE gives easy average-minute interpretation, RMSE highlights larger miss penalties.

Q: Why do we need integration tests if unit tests pass?
A: Most production failures occur at module boundaries, so integration tests are essential.

Q: What quality threshold did you check?
A: The pipeline test validates MAE and R2 thresholds and confirms monotonically increasing arrival times.
