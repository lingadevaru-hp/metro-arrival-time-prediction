# Member 1 - ML Model Logic Building

## Role Summary
You are responsible for how the prediction model works mathematically and why this model was chosen.

## Model Used
We used a **Perceptron-based linear regressor** (single neuron for regression), not a classification perceptron.

Core equation:
- `predicted_segment_time = w1*x1 + w2*x2 + w3*x3 + w4*x4 + b`

Where:
- `x1 = distance_from_prev_km`
- `x2 = avg_speed_kmph`
- `x3 = prev_station_dwell_min`
- `x4 = runtime_min = (distance/speed)*60`

Training method:
- Gradient descent on squared error loss
- Feature scaling (mean/std normalization)
- Optional L2 regularization for stability

## Your Owned Files (Show These)
- `src/metro_perceptron/model.py`
- `src/metro_perceptron/features.py`

## What You Should Explain in Review
1. We converted metro movement into a segment-time prediction problem.
2. We engineered practical transport features from business inputs.
3. We trained a linear neuron because scheduling is mostly linear with these inputs.
4. We used normalized features so training converges fast and reliably.

## Exact Speaking Script
"My part was model logic building. We used a perceptron-style linear regressor to predict travel time between two stations. The feature vector uses distance, speed, previous dwell, and computed runtime. The model learns weights with gradient descent, and we included feature scaling and regularization for stable learning. This gives an interpretable and fast model suitable for operational metro scheduling."

## Demo Points
- Open `src/metro_perceptron/features.py` and show `build_feature_vector(...)`.
- Open `src/metro_perceptron/model.py` and show `fit(...)` and `predict_one(...)`.

## Likely Questions and Answers
Q: Why linear model?
A: Inputs are physically related to time in a near-linear way, so linear regression is a strong baseline and easy to interpret.

Q: Why include runtime feature if distance and speed already exist?
A: It gives the model a direct physics-inspired signal and improves fit quality.
