# Sri Lanka & Canada Tracker
Interactive aircraft map with a Python backend and optional C++ geographic kernel.

## Problem
Public aircraft data is freely available but can be difficult to explore in one simple interface. This project demonstrates a cross-country map with aircraft filters.

## Architecture
- Data: adsb.lol community API
- Backend: Python and FastAPI
- C++20 kernel: batch great-circle distances, loaded through ctypes
- Frontend: Leaflet map with periodic refresh
- Tests: pytest and GitHub Actions

## Engineering choices
- Python fallback if the C++ library is not built
- Demo mode and sample data if the API is unavailable
- Filters for aircraft categories and supported airline callsigns

## Next steps
Validate airport data, improve map views for each region, add historical replay, and monitor API availability.
