# Sri Lanka and Canada Airtracker + Cabin Crew Simulator

A compact aviation project with two visitor-facing features: an aircraft map focused on Sri Lanka and Canada, and an interactive cabin-crew situational-judgment simulator.

## Visitor experience

- Explore aircraft, region/category/airline filters, airport markers and illustrative route corridors.
- Practise three fictional passenger-service situations.
- Read immediate feedback about empathy, communication, safety awareness and escalation.

## Architecture

- Backend: Python and FastAPI
- Frontend: HTML, CSS, JavaScript and Leaflet
- Aircraft data: adsb.lol community API with demo/sample fallback
- Optional C++20 geographic-distance module loaded through ctypes
- Tests: pytest and GitHub Actions

## Engineering choices

- Demo mode allows the project to be explored without depending on live aircraft data.
- The cabin crew simulator runs in the browser and does not require a login.
- Scenario scores are for reflection only; this is not an official airline assessment or training resource.

## Limitations

Aircraft positions may be sample data if the external service is unavailable. Route corridors are illustrative rather than official airways. The project is not intended for operational aviation use.
