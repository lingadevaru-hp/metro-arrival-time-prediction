# Member 3 - Dataset / Database

## What You Actually Built
- Designed the dataset schema for metro stop and segment behavior.
- Prepared the initial sample dataset for one complete line.
- Implemented CSV loader with strong type conversion.
- Implemented SQLite write and read operations for persistence.
- Enforced ordered station sequencing for correct scheduling.

## Data Model You Should Explain
Dataset columns:
- `line_name` for multi-line support.
- `station_order` for correct path sequence.
- `station_name` for readable outputs.
- `distance_from_prev_km` for travel distance input.
- `avg_speed_kmph` for operational speed input.
- `dwell_time_min` for station halt time.
- `observed_segment_time_min` as supervised training target.

Database table:
- `metro_stops`
- Primary key `(line_name, station_order)` to prevent duplicates.

## Files You Own (Show in Presentation)
- `data/metro_line.csv`
- `src/metro_perceptron/data.py`

## 2-Minute Speaking Script (Ready to Read)
"I handled dataset and database work. I first designed the schema so that every station record includes all operational variables needed for arrival prediction, such as distance, speed, and dwell time, plus observed segment time for training.  
I created the CSV dataset as the editable source of truth and then built a data layer to load records with correct numeric types and sorted station order.  
To support persistence and structured querying, I added SQLite integration with a `metro_stops` table and a composite primary key on line and station order.  
This ensures reproducible inputs for training and supports future expansion when more lines or more records are added."

## What to Show on Screen (Order)
1. Open `data/metro_line.csv` and show the columns.
2. Open `src/metro_perceptron/data.py`.
3. Explain `load_stops_from_csv(...)` and type conversion logic.
4. Explain `write_csv_to_sqlite(...)` and table schema.
5. Explain `load_stops_from_db(...)` and ordered retrieval.

## Key Points If Panel Asks “What Exactly Did You Do?”
- I designed and populated the dataset.
- I implemented data ingestion and validation conversion.
- I implemented database persistence and retrieval.
- I guaranteed ordering and consistency for downstream modules.

## Likely Viva Questions
Q: Why keep both CSV and SQLite?
A: CSV is human-editable and quick for prototyping, while SQLite provides reliable structured storage and queryability.

Q: How do you avoid sequence errors in stations?
A: We always sort and fetch by `station_order`.

Q: How will this scale to multiple metro lines?
A: `line_name` is already part of schema and table key, so multi-line extension is straightforward.
