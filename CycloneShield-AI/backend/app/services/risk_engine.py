from .demo_data import cyclone_payload, now_iso, region_by_id


def estimate_risk(region_id: str) -> dict:
    region = region_by_id(region_id)
    if not region:
        raise KeyError(region_id)
    cyclone = cyclone_payload()
    wind = min(100, cyclone["wind_speed_kmh"] / 1.5)
    coastal = region["coastal_exposure"]
    population = region["population_exposure"]
    rainfall = region["rainfall_exposure"]
    score = round(wind * 0.30 + coastal * 0.28 + population * 0.22 + rainfall * 0.12 + region["wind_exposure"] * 0.08, 1)
    level = "CRITICAL" if score >= 80 else "HIGH" if score >= 60 else "MEDIUM" if score >= 35 else "LOW"
    factors = [
        {"name": "Wind exposure", "value": f"{cyclone['wind_speed_kmh']} km/h demo wind", "contribution": round(wind * 0.30, 1), "available": True, "explanation": "Derived from the demonstration cyclone intensity and regional wind exposure."},
        {"name": "Coastal exposure", "value": f"{coastal}/100", "contribution": round(coastal * 0.28, 1), "available": True, "explanation": "Prototype coastal proximity and low-elevation exposure indicator."},
        {"name": "Population exposure", "value": f"{population}/100", "contribution": round(population * 0.22, 1), "available": True, "explanation": "Sample population exposure index, not a damage estimate."},
        {"name": "Rainfall signal", "value": f"{rainfall}/100", "contribution": round(rainfall * 0.12, 1), "available": True, "explanation": "Sample rainfall exposure indicator; no live rainfall feed is enabled."},
        {"name": "Elevation", "value": f"{region['elevation_m']} m", "contribution": round((100 - min(region["elevation_m"], 100)) * 0.08, 1), "available": True, "explanation": "Low elevation can increase coastal-flooding exposure, but this is not a flood forecast."},
    ]
    return {
        "region": region["name"],
        "risk_score": score,
        "risk_level": level,
        "exposure_not_damage": True,
        "data_mode": "DEMO",
        "factors": factors,
        "limitations": [
            "This is a transparent demonstration exposure estimate, not predicted damage.",
            "The cyclone track and intensity are prototype sample data, not an official forecast.",
            "Live rainfall, elevation, population, and shelter feeds are not enabled in this MVP.",
        ],
        "last_updated": now_iso(),
    }
