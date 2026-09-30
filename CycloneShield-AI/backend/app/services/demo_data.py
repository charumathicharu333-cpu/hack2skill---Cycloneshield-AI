from datetime import UTC, datetime


def now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def cyclone_payload() -> dict:
    return {
        "id": "demo-bay-001",
        "name": "Demo Cyclone Varuna",
        "status": "Prototype scenario",
        "data_mode": "DEMO",
        "source": "CycloneShield deterministic demo dataset",
        "last_updated": "2026-09-29T10:30:00Z",
        "latitude": 16.8,
        "longitude": 84.2,
        "wind_speed_kmh": 118,
        "pressure_hpa": 972,
        "movement": "NW at 14 km/h",
        "track": [
            {"latitude": 13.1, "longitude": 88.0, "timestamp": "2026-09-28T04:00:00Z", "wind_speed_kmh": 74},
            {"latitude": 14.2, "longitude": 86.9, "timestamp": "2026-09-28T16:00:00Z", "wind_speed_kmh": 86},
            {"latitude": 15.5, "longitude": 85.6, "timestamp": "2026-09-29T04:00:00Z", "wind_speed_kmh": 104},
            {"latitude": 16.8, "longitude": 84.2, "timestamp": "2026-09-29T10:30:00Z", "wind_speed_kmh": 118},
        ],
        "forecast_track": [
            {"latitude": 18.0, "longitude": 82.8, "timestamp": "2026-09-29T16:00:00Z", "wind_speed_kmh": 122},
            {"latitude": 19.2, "longitude": 81.6, "timestamp": "2026-09-30T04:00:00Z", "wind_speed_kmh": 112},
            {"latitude": 20.0, "longitude": 80.4, "timestamp": "2026-09-30T16:00:00Z", "wind_speed_kmh": 94},
        ],
        "forecast_note": "Prototype forecast path for demonstration only. It is not an official weather warning or operational forecast.",
    }


REGIONS = [
    {
        "id": "visakhapatnam",
        "name": "Visakhapatnam Coast",
        "state": "Andhra Pradesh",
        "latitude": 17.69,
        "longitude": 83.22,
        "population_exposure": 78,
        "elevation_m": 18,
        "coastal_exposure": 82,
        "rainfall_exposure": 65,
        "wind_exposure": 76,
    },
    {
        "id": "kakinada",
        "name": "Kakinada Coast",
        "state": "Andhra Pradesh",
        "latitude": 16.99,
        "longitude": 82.25,
        "population_exposure": 64,
        "elevation_m": 9,
        "coastal_exposure": 90,
        "rainfall_exposure": 69,
        "wind_exposure": 72,
    },
    {
        "id": "chennai",
        "name": "Chennai Coast",
        "state": "Tamil Nadu",
        "latitude": 13.08,
        "longitude": 80.27,
        "population_exposure": 92,
        "elevation_m": 7,
        "coastal_exposure": 73,
        "rainfall_exposure": 58,
        "wind_exposure": 42,
    },
]

RESOURCES = [
    {"id": "s-001", "name": "Demo Coastal Relief School", "resource_type": "Shelter", "region": "Visakhapatnam Coast", "latitude": 17.72, "longitude": 83.29, "status": "Sample location", "contact": "Verify with local authorities", "data_mode": "DEMO", "verification_note": "Sample record. Availability and capacity are not verified."},
    {"id": "h-001", "name": "Demo District Hospital", "resource_type": "Hospital", "region": "Kakinada Coast", "latitude": 16.98, "longitude": 82.25, "status": "Sample location", "contact": "Verify local number", "data_mode": "DEMO", "verification_note": "Sample record. Do not use as a live dispatch directory."},
    {"id": "e-001", "name": "Demo Emergency Coordination Point", "resource_type": "Emergency Service", "region": "Chennai Coast", "latitude": 13.08, "longitude": 80.28, "status": "Sample location", "contact": "Call official emergency services", "data_mode": "DEMO", "verification_note": "Sample record. Use official government guidance for real incidents."},
]


def region_by_id(region_id: str) -> dict | None:
    return next((r for r in REGIONS if r["id"] == region_id), None)
