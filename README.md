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

## Royalty-free media and scroll video wall
The Safety & Video Lab uses externally hosted stock photos and video previews from Pexels. The scroll video wall lazy-loads clips as they approach the viewport, starts them muted when visible (multiple visible clips may play together), and pauses clips after they leave the viewport. Tap/click a video to pause or resume it using the player controls. Autoplay may be restricted by browser settings, data saver, or iOS low-power mode; the Pexels source links remain available as fallbacks.

Pexels states that its photos and videos are free to use under the Pexels License, without required attribution. Rights to identifiable people, logos, and other depicted content may be separate, so review the source page and license before republishing or using footage in a commercial context. This project embeds source-hosted media rather than repackaging or redistributing the stock files. See the [Pexels License](https://www.pexels.com/license/) and [Pexels video library](https://www.pexels.com/videos/).

The remote MP4 variants are best-effort previews; if a direct file URL changes or is unavailable, use the source link under the video. Browser autoplay requires muted video and does not guarantee playback on every device/network.

## Additional Wikimedia Commons media

The Safety & Video Lab includes an open-license gallery with direct in-page playback for two short clips and three full-frame aircraft photos. Each media card links to its source file page, which is the authoritative record for creator credit and licensing. The clips use native controls and do not autoplay.

- **Boeing BBJ 737-700 N301SR MD1.jpg** — creator: Acroterion; CC BY-SA 4.0. [Source and licence](https://commons.wikimedia.org/wiki/File:Boeing_BBJ_737-700_N301SR_MD1.jpg).
- **Plane, Boeing 737 900 ER.jpg** — creator: Haaan22; CC BY-SA 4.0. [Source and licence](https://commons.wikimedia.org/wiki/File:Plane,_Boeing_737_900_ER.jpg).
- **Boeing 777.jpg** — [source file page and licence details](https://commons.wikimedia.org/wiki/File:Boeing_777.jpg); retain the attribution and terms shown on the source page.
- **Kathmandu airport landing night.webm** — creator: Ventriloquist; CC BY-SA 4.0. [Source and licence](https://commons.wikimedia.org/wiki/File:Kathmandu_airport_landing_night.webm).
- **PlanePassingThunderCloud.ogv** — creator: Docfirerock; CC BY-SA 4.0. [Source and licence](https://commons.wikimedia.org/wiki/File:PlanePassingThunderCloud.ogv).

Creative Commons Attribution-ShareAlike media requires appropriate credit, a licence link and an indication of changes where applicable; adapted material may also need to be shared under the same or a compatible licence. Review the individual file page before redistribution or modification. Existing Pexels-hosted media remains subject to the Pexels licence and any separate rights in depicted people, marks or other content.

## Media reliability and visual clarity
Safety cards use larger, high-contrast imagery for at-a-glance viewing. If a remotely hosted photo fails, the UI substitutes an original animated SVG aviation illustration. The video wall attempts lazy-loaded stock footage; on a media error or a 12-second load timeout it replaces the failed player with an animated original illustration instead of showing a “hosted preview unavailable” message. Animation pauses while the card is outside the viewport and can be paused/resumed by tapping the illustration. Remote stock previews depend on third-party hosting; source links are provided for original media. The animated SVG scenes are generated by the app and do not require an external image license.


## Licensed media and full-frame viewing
The six passenger-safety photos are embedded directly in the cards and do not navigate away when tapped or clicked. They use `object-fit: contain` so the complete photo is visible without cropping. Video cards retain source links to original Pexels clips. Pexels states its photos and videos are available for free use under the Pexels License; this is not a blanket clearance for separate rights in logos, brands, or identifiable people. If third-party media fails to load, original animated SVG illustrations provide a local fallback. Review the [Pexels License](https://www.pexels.com/license/) and the source page for each item before commercial reuse.


## Vector tracking and exploration engine

The repository now includes `exploration_engine.py`, a dependency-free Python reference module implementing vector tracking, angle-threshold turn/change detection, and 2D occupancy-grid raycasting, plus `tests/test_exploration_engine.py` covering normal cases and invalid inputs.

- **Use case:** aircraft/map exploration; translate project measurements into 2D coordinates before interpreting the generic algorithm's results.
- **Run tests:** `python -m pytest -q`.
- **Scope:** this raycast is a generic grid primitive, not geographic collision avoidance, official aviation routing, medical advice, or real-world navigation.

The existing GitHub repository and live-demo URLs remain unchanged. Python is the implemented reference engine. C++23 with Conan/vcpkg, Rust, PHP/Symfony/Mago, and Django are not represented as integrated runtimes in this change; they should be added only as tested adapters where the project's architecture benefits from them, rather than forcing every framework into every app.
