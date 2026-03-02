Nanditha - ML Model Logic Building

## What You Actually Built
- Defined the prediction target as `segment travel time in minutes` from previous station to current station.
- Finalized the feature set used by the model.
- Designed and implemented a perceptron-style linear regression training approach.
- Added model stability features: input normalization, L2 regularization, and convergence tolerance.

## Model Explanation You Should Say
We used a **Perceptron-based linear regressor** (single neuron for regression), not a classification perceptron.

Equation:
- `predicted_segment_time = w1*x1 + w2*x2 + w3*x3 + w4*x4 + b`

Feature mapping:
- `x1 = distance_from_prev_km`
- `x2 = avg_speed_kmph`
- `x3 = prev_station_dwell_min`
- `x4 = runtime_min = (distance/speed)*60`

Training:
- Minimized squared error using gradient descent.
- Normalized features with mean/std scaling before training.
- Applied small L2 penalty to avoid unstable large weights.

## Files You Own (Show in Presentation)
- `src/metro_perceptron/features.py`
- `src/metro_perceptron/model.py`

## 2-Minute Speaking Script (Ready to Read)
"I handled ML model logic building. First, I converted the business problem into a supervised regression task where each training sample is one metro segment and the target is segment travel time in minutes.  
I designed the feature vector using distance, average speed, previous station dwell time, and a derived runtime feature `(distance/speed)*60`. This gives both operational and physics-based signals.  
For modeling, I implemented a perceptron-style linear regressor. The model learns weights using gradient descent on squared error loss. To make training stable, I added feature scaling and optional L2 regularization, and I stop when loss improvement becomes very small.  
This model is simple, fast, and interpretable, which is useful for transportation scheduling where we need understandable decisions, not a black-box model."

## What to Show on Screen (Order)
1. Open `src/metro_perceptron/features.py`.
2. Show `build_feature_vector(...)` and explain each feature.
3. Show `build_training_data(...)` and explain segment-level formulation.
4. Open `src/metro_perceptron/model.py`.
5. Show `fit(...)` for scaling + gradient descent.
6. Show `predict_one(...)` for inference formula.

## Key Points If Panel Asks “What Exactly Did You Do?”
- I defined problem framing and target variable.
- I selected and engineered model features.
- I implemented model training logic and prediction logic.
- I added training safeguards for stable convergence.

## Likely Viva Questions
Q: Why did you choose linear perceptron instead of deep learning?
A: The relationship between travel time, distance, speed, and dwell is mostly linear at baseline, so linear models are strong, explainable, and fast for this scope.

Q: Why normalize features?
A: Features are on different scales, and normalization makes gradient descent stable and faster.

Q: Why use both speed and runtime feature?
A: Runtime adds a direct domain formula signal and improves fit consistency.
