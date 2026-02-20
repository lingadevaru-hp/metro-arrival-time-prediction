# Member 3 - Dataset / Database

## Role Summary
You are responsible for creating the dataset and database layer for reliable input handling.

## Data Design
Dataset columns:
- `line_name`
- `station_order`
- `station_name`
- `distance_from_prev_km`
- `avg_speed_kmph`
- `dwell_time_min`
- `observed_segment_time_min`

Database design:
- SQLite table: `metro_stops`
- Primary key: `(line_name, station_order)`

## Your Owned Files (Show These)
- `data/metro_line.csv`
- `src/metro_perceptron/data.py`

## What You Should Explain in Review
1. We created realistic station-level records with travel-relevant attributes.
2. CSV is used as source data for easy editing and auditing.
3. SQLite is used for persistent storage and future query-based workflows.
4. Data loader enforces numeric conversion and station ordering.

## Exact Speaking Script
"My part was dataset and database handling. I prepared the metro station dataset with distance, speed, dwell, and observed segment time. Then I built loader functions for CSV and SQLite so the project has both editable raw data and structured persistent storage. This ensures data consistency and reproducible model runs."

## Demo Points
- Open `data/metro_line.csv` and show column design.
- Open `src/metro_perceptron/data.py` and show `load_stops_from_csv(...)` and `write_csv_to_sqlite(...)`.

## Likely Questions and Answers
Q: Why SQLite for this project?
A: It is lightweight, portable, and enough for a prototype database layer.

Q: What ensures correct station sequence?
A: We sort by `station_order` after loading.
