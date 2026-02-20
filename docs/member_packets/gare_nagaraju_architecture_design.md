# Gare Nagaraju - Architecture Design

## What You Actually Built
- Designed the complete system flow from raw data to predicted timetable.
- Broke the project into independent modules so each team member can own one part.
- Defined interfaces between layers to avoid tight coupling.
- Documented architecture so reviewers can understand design decisions quickly.

## Architecture You Should Explain
End-to-end flow:
- Data Layer -> Feature Layer -> Model Layer -> Scheduler Layer -> Interface Layer

Layer responsibilities:
- Data Layer: load CSV and optional SQLite persistence.
- Feature Layer: convert stop records into segment-level training vectors.
- Model Layer: train/predict segment minutes.
- Scheduler Layer: accumulate minutes into actual arrival and departure times.
- Interface Layer: CLI output and Streamlit UI.

Why this design:
- Easier debugging because each layer can be tested separately.
- Easier collaboration because ownership is clean.
- Easier extension because model or data source can be replaced without rewriting everything.

## Files You Own (Show in Presentation)
- `docs/architecture.md`
- `README.md`
- `src/metro_perceptron/__init__.py`

## 2-Minute Speaking Script (Ready to Read)
"I handled architecture design for this project. I designed the system as a modular pipeline so each phase has a clear responsibility.  
The data layer handles ingestion and storage, the feature layer transforms raw station data into learning vectors, the model layer predicts segment travel time, and the scheduler layer converts those predictions into station-wise arrival and departure times.  
I intentionally separated these components so we can test each layer independently and easily replace parts in the future, for example replacing CSV with live API feeds or replacing the model with a more advanced algorithm.  
This architecture made team collaboration cleaner and made the final system easier to maintain and explain."

## What to Show on Screen (Order)
1. Open `docs/architecture.md`.
2. Explain the flow diagram line by line.
3. Open `README.md` and show the project folder structure.
4. Open `src/metro_perceptron/__init__.py` to show module boundaries.

## Key Points If Panel Asks “What Exactly Did You Do?”
- I defined module boundaries and data flow contracts.
- I ensured model logic and scheduling logic are decoupled.
- I designed for maintainability, testability, and future scalability.
- I documented the architecture for quick onboarding.

## Likely Viva Questions
Q: Why not keep everything in a single file for a small project?
A: A modular design prevents technical debt and supports team-based development and testing.

Q: If live metro data comes tomorrow, what changes?
A: Primarily the data layer changes. Feature/model/scheduler layers can remain the same.

Q: Where is failure isolation in this architecture?
A: Each layer has independent functions, so failures can be traced quickly to a specific module.
