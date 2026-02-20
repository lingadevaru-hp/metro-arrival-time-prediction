# Achyuth - Model Implementation

## What You Actually Built
- Connected all modules into one executable training and prediction pipeline.
- Implemented schedule generation logic from start departure time.
- Converted segment predictions into station arrival and departure timeline.
- Added runtime safety checks for valid schedule outputs.

## Implementation Details You Should Explain
Pipeline execution:
- Load dataset.
- Build training vectors.
- Train perceptron regressor.
- Predict segment times.
- Compute metrics.
- Generate station-wise schedule from user input start time.

Scheduler logic:
- Station 1 arrival is equal to user-provided start departure.
- For each next station, add predicted segment minutes to current time.
- Add station dwell minutes for departure display.
- Clamp segment prediction using `max(0, prediction)` to avoid negative durations.

## Files You Own (Show in Presentation)
- `scripts/run_demo.py`
- `src/metro_perceptron/scheduler.py`
- `src/metro_perceptron/model.py`

## 2-Minute Speaking Script (Ready to Read)
"I handled implementation of the working pipeline. I integrated data loading, feature creation, model training, prediction, and final schedule output into one executable flow.  
In the scheduler module, I convert predicted segment minutes into real clock times using the starting departure input. For each station, arrival is calculated by accumulating predicted travel minutes, and departure includes station dwell time.  
I also added practical constraints like non-negative segment duration handling to keep outputs operationally valid.  
So my contribution was converting model logic into a usable end-to-end timetable generation system."

## What to Show on Screen (Order)
1. Run `python scripts/run_demo.py --departure 08:30`.
2. Explain printed metrics and schedule table.
3. Open `scripts/run_demo.py` and show pipeline sequence.
4. Open `src/metro_perceptron/scheduler.py` and explain `predict_arrival_schedule(...)`.
5. Point out the non-negative clamp and dwell handling.

## Key Points If Panel Asks “What Exactly Did You Do?”
- I assembled the complete execution flow.
- I transformed ML outputs into practical schedule times.
- I implemented safe scheduling rules and reproducible script interface.
- I made sure user input time dynamically shifts full route timeline.

## Likely Viva Questions
Q: What input does the user control in your implementation?
A: The start departure time; it shifts the complete predicted timetable.

Q: Why does scheduler need separate logic from model?
A: Model predicts segment duration only. Scheduler converts durations into station timestamps.

Q: What prevents impossible outputs?
A: Negative duration protection and ordered station traversal.
