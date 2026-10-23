# Sri Lanka and Canada Airtracker + Cabin Crew Simulator

A responsive aviation portfolio demo combining an aircraft explorer with a futuristic public safety learning lab and cabin-crew scenario simulator.

## Live demo
https://srilanka-canada-airtracker.vercel.app

## Features
- Interactive aircraft map for Sri Lanka and Canada using Leaflet.
- Aircraft filters, airport markers and illustrative route corridors.
- Cabin Crew Simulator with fictional passenger-service scenarios and feedback.
- Futuristic animated Safety & Video Lab tab.
- Public passenger safety explainers: seat belts, exits, oxygen masks, life vests, turbulence and evacuation.
- Five interactive safety knowledge-check scenarios.
- Readiness checklist with progress indicator.
- Local video preview for your own landing/safety clips. Files remain in your browser during the session and are not uploaded by this static demo.
- Public-facing cabin-crew role explainers and links to FAA/IATA safety resources.

## Add your own videos
Open the demo and choose **Safety & Video Lab**, then select video files from your device. MP4 or WebM is recommended. This is a local preview feature. To make your clips visible to every visitor, only use videos you own or are licensed to publish and upload them to a public video host or the repository, then add the hosted video reference to the site. The current demo does not generate video files itself.

## Run locally
Requirements: Python 3.10+ and pip. A C++ compiler and make are optional.

    python -m pip install -r requirements.txt
    DEMO=1 python -m uvicorn backend.app.main:app --reload

Open http://127.0.0.1:8000. Run tests with:

    python -m pytest -q

Optional C++ module: run `make` with g++ 11+ and make installed.

## Data notes
Without `DEMO=1`, the aircraft map attempts to query the public adsb.lol community API and falls back to sample data if unavailable. Live data depends on that external service. Airport coordinates should be verified before use; route corridors are illustrative straight lines, not official airways. This is an educational demo, not an aviation safety or dispatch tool.

## Safety and scope
The safety lab provides broad passenger-facing guidance, not confidential airline procedures. It does not replace aircraft-specific safety cards, airline manuals, regulator requirements, certification, or instructor-led training. Procedures vary by aircraft and airline; follow the operating crew. Any AI-generated scenes should be labelled as simulations and should not be presented as official airline footage.

## Project layout
- `backend/app/`: FastAPI endpoints and processing logic
- `frontend/index.html`: aircraft map, cabin crew simulator and safety/video lab
- `cpp/`: optional C++ geographic-distance implementation
- `data/`: airport reference data and sample aircraft
- `tests/`: pytest tests
- `.github/workflows/`: GitHub Actions CI
- `render.yaml`: Render deployment blueprint

## License
MIT. See `LICENSE`.
