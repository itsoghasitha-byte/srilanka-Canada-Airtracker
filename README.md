# Sri Lanka and Canada Airtracker + Cabin Crew Simulator

This project combines two interactive demos: an aircraft explorer focused on Sri Lanka and Canada, and a **Cabin Crew Simulator** for practising passenger-service decisions.

The simulator presents short fictional scenarios and gives feedback on empathy, clear communication, safety awareness and appropriate escalation. It is a small learning and portfolio demo—not an airline hiring test or a replacement for official training.

## Try the demo

**Live demo:** the public URL will be added here once deployment has completed successfully. Until then, you can run the app locally.

## Features

- **Sri Lanka and Canada Airtracker:** explore aircraft by region, filter by aircraft category or airline, and view airport markers and illustrative route corridors.
- **Cabin Crew Simulator:** practise responses to a worried passenger during turbulence, a complaint about a delayed flight, and a passenger who appears unwell.
- **Scenario feedback:** review the reasoning behind each choice and a simple practice score.
- **API and engineering:** FastAPI endpoints, pytest tests, GitHub Actions CI and an optional C++20 geographic-distance module.

## How to use it

1. Open the live demo link above when it is available.
2. Select **Cabin Crew Simulator** to begin. No account is needed.
3. Read the situation and choose the response you would take.
4. Review the feedback, then continue to the next scenario or restart.
5. Select **Sri Lanka and Canada Airtracker** to explore aircraft and filters.

Scenarios are fictional examples for reflection. Scores do not predict recruitment outcomes or certify suitability for cabin-crew work.

## Run locally

Requirements: Python 3.10+ and pip. A C++ compiler and make are optional.

    python -m pip install -r requirements.txt
    DEMO=1 python -m uvicorn backend.app.main:app --reload

Open http://127.0.0.1:8000. Run tests with:

    python -m pytest -q

Optional C++ module: run `make` with g++ 11+ and make installed.

## Data notes

Without `DEMO=1`, the aircraft map attempts to query the public adsb.lol community API and falls back to sample data if unavailable. Live data depends on that external service. Airport coordinates should be verified before use; route corridors are illustrative straight lines, not official airways. This is an educational demo, not an aviation safety or dispatch tool.

## Project layout

- `backend/app/`: FastAPI endpoints and processing logic
- `frontend/index.html`: aircraft map and cabin crew simulator
- `cpp/`: optional C++ geographic-distance implementation
- `data/`: airport reference data and sample aircraft
- `tests/`: pytest tests
- `.github/workflows/`: GitHub Actions CI
- `render.yaml`: Render deployment blueprint

## License

MIT. See `LICENSE`.
