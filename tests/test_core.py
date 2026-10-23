import os
os.environ["DEMO"] = "1"
from backend.app import core

def test_distance_toronto_montreal():
    d = core.distances_km([45.470], [-73.741], 43.677, -79.631)[0]
    assert 500 < d < 510

def test_classify():
    assert core.classify("c172") == "small"
    assert core.classify("GLF6") == "bizjet"
    assert core.classify("B738") == "other"

def test_normalize_drops_no_position_and_ground_altitude():
    assert core.normalize({"hex": "x", "lat": None, "lon": None}) is None
    assert core.normalize({"hex": "x", "lat": 1, "lon": 2, "alt_baro": "ground"})["alt_ft"] == 0

def test_aircraft_filters():
    assert len(core.aircraft("toronto", "all")) == 7
    assert [a["type"] for a in core.aircraft("toronto", "small")] == ["C172", "PC12"]

def test_corridors_and_airports():
    assert len(core.corridors()) == 13
    assert len(core.airports()) == 20

def test_airline_filter_and_sri_lanka_region():
    assert [a["callsign"] for a in core.aircraft("toronto", "all", "aca")] == ["ACA123"]
    assert {a["airline"] for a in core.aircraft("colombo")} >= {"SriLankan Airlines", "FitsAir"}
    assert "colombo" in core.REGIONS
