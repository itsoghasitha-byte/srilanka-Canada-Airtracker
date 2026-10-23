from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from . import core

app = FastAPI(
    title="Tracjer",
    description="Aircraft exploration for Sri Lanka and Canada, plus interactive cabin-crew scenario practice.",
    version="1.1.0",
)
FRONTEND = Path(__file__).resolve().parents[2] / "frontend" / "index.html"

@app.get("/api/aircraft")
def get_aircraft(region: str = "toronto", category: str = "all", airline: str | None = None):
    if region not in core.REGIONS:
        raise HTTPException(404, f"region must be one of {list(core.REGIONS)}")
    if category not in {"all", "small", "bizjet", "other"}:
        raise HTTPException(400, "category must be all, small, bizjet, or other")
    return core.aircraft(region, category, airline)

@app.get("/api/airlines")
def get_airlines():
    return core.AIRLINES

@app.get("/api/airports")
def get_airports():
    return core.airports()

@app.get("/api/corridors")
def get_corridors():
    return core.corridors()

@app.get("/health")
def health():
    return {"status": "ok", "app": "Tracjer"}

@app.get("/")
def index():
    return FileResponse(FRONTEND)
