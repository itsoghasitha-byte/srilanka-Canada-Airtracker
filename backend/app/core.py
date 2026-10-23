"""Core logic: fetch, normalise, classify and measure aircraft."""
import csv
import ctypes
import json
import math
import os
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SMALL = {"C150", "C152", "C172", "C182", "C206", "C208", "PA28", "PA32", "PA34", "SR20", "SR22", "BE36", "DA40", "DA42", "PC12", "TBM9", "P28A", "M20P"}
BIZJET = {"C25A", "C25B", "C510", "C525", "C56X", "C680", "C750", "CL30", "CL35", "CL60", "E50P", "E55P", "GLF4", "GLF5", "GLF6", "FA7X", "FA8X", "LJ45", "H25B", "GL7T"}
REGIONS = {"toronto": (43.68, -79.63), "vancouver": (49.19, -123.18), "montreal": (45.47, -73.74), "calgary": (51.11, -114.02), "winnipeg": (49.91, -97.24), "halifax": (44.88, -63.51), "colombo": (7.18, 79.88)}
AIRLINES = {"ACA": "Air Canada", "WJA": "WestJet", "POE": "Porter", "TSC": "Air Transat", "ALK": "SriLankan Airlines", "EXV": "FitsAir"}

try:
    _lib = ctypes.CDLL(str(Path(__file__).with_name("libgeo.so")))
    _lib.haversine_batch.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.POINTER(ctypes.c_double)]
except OSError:
    _lib = None

def _py_haversine(lat, lon, lat0, lon0):
    p0 = math.radians(lat0)
    out = []
    for la, lo in zip(lat, lon):
        p1, dl = math.radians(la), math.radians(lo - lon0)
        a = math.sin((p1 - p0) / 2) ** 2 + math.cos(p0) * math.cos(p1) * math.sin(dl / 2) ** 2
        out.append(2 * 6371.0088 * math.asin(math.sqrt(min(1.0, a))))
    return out

def distances_km(lat, lon, lat0, lon0):
    if _lib is None or not lat:
        return _py_haversine(lat, lon, lat0, lon0)
    n = len(lat)
    A, B, O = (ctypes.c_double * n)(*lat), (ctypes.c_double * n)(*lon), (ctypes.c_double * n)()
    _lib.haversine_batch(A, B, n, lat0, lon0, O)
    return list(O)

def classify(type_code):
    t = (type_code or "").upper()
    return "small" if t in SMALL else "bizjet" if t in BIZJET else "other"

def normalize(ac):
    if ac.get("lat") is None or ac.get("lon") is None:
        return None
    alt = ac.get("alt_baro")
    flight = (ac.get("flight") or "").strip()
    return {"id": ac.get("hex"), "callsign": flight, "airline": AIRLINES.get(flight[:3].upper()), "type": ac.get("t"), "category": classify(ac.get("t")), "lat": ac["lat"], "lon": ac["lon"], "alt_ft": alt if isinstance(alt, (int, float)) else 0, "speed_kt": ac.get("gs")}

def _sample():
    return json.loads((ROOT / "data" / "sample_aircraft.json").read_text())

def fetch_raw(lat, lon, radius_nm=250):
    if os.getenv("DEMO") == "1":
        return _sample()
    url = f"https://api.adsb.lol/v2/point/{lat}/{lon}/{radius_nm}"
    req = urllib.request.Request(url, headers={"User-Agent": "sri-lanka-canada-tracker"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.load(r)

def aircraft(region="toronto", category="all", airline=None):
    lat0, lon0 = REGIONS[region]
    try:
        raw = fetch_raw(lat0, lon0)
    except Exception:
        raw = _sample()
    items = [x for x in map(normalize, raw.get("ac", [])) if x]
    dists = distances_km([i["lat"] for i in items], [i["lon"] for i in items], lat0, lon0)
    for it, d in zip(items, dists):
        it["km_from_center"] = round(d, 1)
    items = [i for i in items if category in ("all", i["category"])]
    return [i for i in items if not airline or i["callsign"][:3].upper() == airline.upper()]

def airports():
    with open(ROOT / "data" / "airports.csv", newline="") as f:
        return list(csv.DictReader(f))

def corridors():
    ap = {a["iata"]: a for a in airports()}
    pairs = [("YVR", "YYZ"), ("YYZ", "YUL"), ("YYC", "YYZ"), ("YYZ", "YHZ"), ("YYZ", "LHR"), ("YUL", "CDG"), ("YYZ", "JFK"), ("YVR", "HND"), ("YYZ", "DXB"), ("YVR", "SIN"), ("CMB", "DXB"), ("CMB", "SIN"), ("CMB", "LHR")]
    pt = lambda c: [float(ap[c]["lat"]), float(ap[c]["lon"])]
    return [{"from": a, "to": b, "path": [pt(a), pt(b)]} for a, b in pairs]
