# Khushi - UI & Documentation

## What You Actually Built
- Created an interactive Streamlit interface for live demo.
- Added user controls for hyperparameters and starting departure time.
- Displayed prediction quality metrics and schedule output in readable format.
- Wrote clear documents for setup, architecture, and role-wise ownership.

## UI/Documentation Explanation You Should Say
UI functionality:
- User can adjust `learning_rate`, `epochs`, and start time.
- Model retrains and updates metrics in the same screen.
- Predicted schedule is shown in a clear station table.

Documentation functionality:
- `README.md` gives setup and run commands.
- `docs/architecture.md` explains system flow.
- `docs/member_work_guide.md` and packet files map ownership and presentation content.

## Files You Own (Show in Presentation)
- `ui/streamlit_app.py`
- `README.md`
- `docs/architecture.md`
- `docs/member_work_guide.md`

## 2-Minute Speaking Script (Ready to Read)
"I handled UI and documentation. I built a Streamlit app so evaluators can interact with the system without reading code first. They can change training parameters and start departure time and immediately see updated metrics and station-wise schedule output.  
On the documentation side, I created clear run instructions, architecture notes, and role-based guides so anyone can reproduce, understand, and present the project quickly.  
My contribution focused on usability and communication, making the technical work accessible to both technical and non-technical reviewers."

## What to Show on Screen (Order)
1. Run `streamlit run ui/streamlit_app.py`.
2. Show sliders and start-time input.
3. Show MAE, RMSE, R2 metrics cards.
4. Show schedule table and explain columns.
5. Open `README.md` and show quick-start commands.

## Key Points If Panel Asks “What Exactly Did You Do?”
- I made the project demo-friendly.
- I ensured outputs are understandable to reviewers.
- I documented how to run, validate, and explain the project.
- I helped convert code deliverables into presentation deliverables.

## Likely Viva Questions
Q: Why is UI important if CLI already exists?
A: UI improves demonstration quality and makes model behavior easy to inspect in real time.

Q: What value did documentation add?
A: It ensures reproducibility, onboarding speed, and clear ownership during evaluation.

Q: Who benefits from this layer most?
A: Reviewers, mentors, and non-developer stakeholders.
