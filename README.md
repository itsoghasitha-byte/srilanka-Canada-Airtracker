# Sri Lanka & Canada Tracker

Sri Lanka & Canada Tracker is an interactive aircraft-tracking demo that maps public aircraft data across both countries. Built with Python, FastAPI, C++20 and Leaflet, it includes aircraft categories, airline filters, airport markers and illustrative routes, with sample data available for local testing.

## Features
- Interactive Leaflet map with Canada and Sri Lanka region options.
- Aircraft category and airline filters.
- Airport markers and illustrative hub-to-hub route corridors.
- FastAPI endpoints for aircraft, airlines, airports and corridors.
- Optional C++20 geographic-distance module with a Python fallback.
- Sample/demo data, pytest tests and GitHub Actions CI.

## Quick start
Requirements: Python 3.10+ and pip. A C++ compiler and make are optional.

```bash
python -m pip install -r requirements.txt
DEMO=1 python -m uvicorn backend.app.main:app --reload
```
Open http://127.0.0.1:8000. To run tests:

```bash
python -m pytest -q
```

Optional C++ module: run `make` with g++ 11+ and make installed.

## Live data and limitations
Without `DEMO=1`, the app attempts to query the public adsb.lol community API and falls back to sample data if unavailable. Live data depends on external service availability and terms. Airport coordinates should be verified before use; route corridors are illustrative straight lines, not official airways. This is an educational demo, not an aviation safety or dispatch tool.

## Project structure
- `backend/app/`: FastAPI endpoints and processing logic
- `cpp/`: optional C++ geographic-distance implementation
- `data/`: airport reference data and sample aircraft
- `frontend/`: Leaflet interactive map
- `tests/`: pytest tests
- `.github/workflows/`: GitHub Actions CI
- `docs/`: presentation and supporting notes

## License
MIT. See `LICENSE`.
