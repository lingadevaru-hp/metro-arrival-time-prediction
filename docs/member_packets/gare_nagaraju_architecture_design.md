# Gare Nagaraju - Architecture Design

## Role Summary
You are responsible for the system design and module flow.

## Architecture Chosen
Pipeline architecture:
- Data Layer -> Feature Layer -> Model Layer -> Scheduler Layer -> Output Layer

Why this architecture:
- Clear separation of concerns
- Easy testing of each layer
- Easy future upgrades (new model, real-time feeds, API deployment)

## Your Owned Files (Show These)
- `docs/architecture.md`
- `README.md`

## What You Should Explain in Review
1. Input sources are structured in a data layer (CSV and SQLite).
2. Feature engineering is isolated from model code.
3. Model only learns segment time, scheduler converts it into real arrival timestamps.
4. Interface layer supports both CLI and UI usage.

## Exact Speaking Script
"My responsibility was architecture design. I designed a modular flow from data ingestion to final schedule prediction. We keep feature logic, model training, and schedule generation in separate modules so each part is maintainable and testable. This architecture also supports extension to APIs or real-time transport telemetry later."

## Demo Points
- Open `docs/architecture.md` and show flow steps.
- Open `README.md` and show project structure section.

## Likely Questions and Answers
Q: Why not write everything in one script?
A: Modular architecture reduces complexity, supports team ownership, and improves maintainability.

Q: How can this scale later?
A: Replace CSV with live data source, keep same feature/model/scheduler contracts.
