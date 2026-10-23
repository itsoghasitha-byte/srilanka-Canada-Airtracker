# Tracjer

Tracjer is a small interactive aviation project with two practical views: an aircraft map for Sri Lanka and Canada, and **Cabin Crew Scenarios**, a short situational-judgment practice tool.

The cabin crew module lets visitors work through everyday passenger-service situations and see feedback on communication, empathy, safety awareness and escalation. It is a learning demo—not an airline hiring test or a substitute for official cabin-crew training.

## Try the demo

**Public demo:** once deployment finishes, use the live URL linked from this repository's About section. The public demo link will be added here when a successful deployment URL is confirmed.

## What you can try

- **Aircraft map:** explore regions, aircraft categories, airline filters, airport markers and illustrative route corridors.
- **Cabin Crew Scenarios:** respond to a worried passenger during turbulence, a complaint about a delay, or a passenger who appears unwell.
- **Feedback after each choice:** review the reasoning and a simple skills breakdown for empathy, clear communication, safety awareness and escalation.
- **API:** FastAPI endpoints for aircraft, airlines, airports and corridors.
- **Engineering:** Python, FastAPI, a small optional C++20 geographic-distance module, pytest tests and GitHub Actions CI.

## Use it as a visitor

1. Open the public demo link at the top of this README when it is available.
2. Choose **Cabin Crew Scenarios** to practise a situation; no account is needed.
3. Read the passenger situation and choose the response you would take.
4. Review the feedback and skills breakdown, then try another scenario.
5. Choose **Aircraft Map** to explore the map and its filters.

The scenarios are fictional practice examples. Scores are explanatory feedback only; they do not predict recruitment outcomes or certify suitability for cabin-crew work.

## Run locally

Requirements: Python 3.10+ and pip. A C++ compiler and make are optional.

    python -m pip install -r requirements.txt
    DEMO=1 python -m uvicorn backend.app.main:app --reload

Open http://127.0.0.1:8000. Run the automated tests with:

    python -m pytest -q

Optional C++ module: run make with g++ 11+ and make installed.

## Data notes

Without DEMO=1, the aircraft map attempts to query the public adsb.lol community API and falls back to sample data if unavailable. Live aircraft data depends on the external service and its terms. Airport coordinates should be verified before use; route corridors are illustrative straight lines, not official airways. The map is an educational demo, not an aviation safety or dispatch tool.

## Project layout

- backend/app/: FastAPI endpoints and processing logic
- frontend/index.html: responsive map and cabin-crew scenario experience
- cpp/: optional C++ geographic-distance implementation
- data/: airport reference data and sample aircraft
- tests/: pytest tests
- .github/workflows/: GitHub Actions CI
- render.yaml: Render web-service configuration

## License

MIT. See LICENSE.
