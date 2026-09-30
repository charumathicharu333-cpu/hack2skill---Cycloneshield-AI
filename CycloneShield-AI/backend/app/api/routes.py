from fastapi import APIRouter, HTTPException, Query

from app.schemas.models import (
    CycloneSummary,
    DataStatus,
    ModelMetrics,
    PreparednessResponse,
    Resource,
    RiskResponse,
)
from app.services.demo_data import REGIONS, RESOURCES, cyclone_payload, now_iso, region_by_id
from app.services.risk_engine import estimate_risk

router = APIRouter(prefix="/api")


@router.get("/health")
def health() -> dict:
    return {"status": "ok", "service": "cycloneshield-backend", "mode": "DEMO"}


@router.get("/cyclones", response_model=list[CycloneSummary])
def cyclones() -> list[dict]:
    return [cyclone_payload()]


@router.get("/cyclones/{cyclone_id}", response_model=CycloneSummary)
def cyclone(cyclone_id: str) -> dict:
    item = cyclone_payload()
    if cyclone_id != item["id"]:
        raise HTTPException(status_code=404, detail="Cyclone not found in the selected data source")
    return item


@router.get("/regions")
def regions() -> dict:
    return {"data_mode": "DEMO", "regions": REGIONS}


@router.get("/risk", response_model=RiskResponse)
def risk(
    latitude: float | None = Query(default=None, ge=-90, le=90),
    longitude: float | None = Query(default=None, ge=-180, le=180),
    region: str = Query(default="visakhapatnam"),
) -> dict:
    if latitude is not None and longitude is not None and not (-90 <= latitude <= 90 and -180 <= longitude <= 180):
        raise HTTPException(status_code=422, detail="Latitude or longitude is outside valid geographic bounds")
    try:
        return estimate_risk(region)
    except KeyError as exc:
        raise HTTPException(status_code=404, detail="Unknown demonstration region") from exc


@router.get("/preparedness", response_model=PreparednessResponse)
def preparedness(region: str = Query(default="Visakhapatnam Coast", min_length=2, max_length=100)) -> dict:
    return {
        "region": region,
        "data_mode": "DEMO",
        "guidance": {
            "Residents": [
                "Follow official local warnings and verify evacuation instructions before moving.",
                "Keep drinking water, medicines, torch, power bank, documents, and emergency contacts ready.",
                "Stay indoors away from windows during strong winds; never walk or drive through floodwater.",
            ],
            "Fishermen": [
                "Do not enter the sea when official maritime warnings advise against it.",
                "Check vessel communications, fuel, life jackets, and return-to-shore instructions.",
            ],
            "Farmers": [
                "Secure loose equipment, protect livestock, and move animals to higher safe ground where advised.",
                "Back up important records and inspect drainage around storage areas.",
            ],
            "Response teams": [
                "Confirm shelter status, transport availability, and communications through official channels.",
                "Use this prototype only for prioritization support, never as a replacement for an official incident command system.",
            ],
            "Accessibility": [
                "Plan support for elderly people, children, pregnant people, and people with disabilities.",
                "Keep essential medicines, mobility aids, communication cards, and caregiver contacts together.",
            ],
        },
        "emergency_note": "This prototype does not publish evacuation orders or live emergency phone numbers. Use official government and emergency-service guidance for a real event.",
        "limitations": ["Sample recommendations are general preparedness guidance, not a personalized order or guarantee of safety."],
    }


@router.get("/resources", response_model=list[Resource])
def resources(region: str | None = Query(default=None, max_length=100), resource_type: str | None = Query(default=None, max_length=40)) -> list[dict]:
    values = RESOURCES
    if region:
        values = [item for item in values if item["region"].lower() == region.lower()]
    if resource_type:
        values = [item for item in values if item["resource_type"].lower() == resource_type.lower()]
    return values


@router.get("/data-status", response_model=DataStatus)
def data_status() -> dict:
    return {
        "mode": "DEMO",
        "live_provider": "Not configured",
        "live_available": False,
        "last_checked": now_iso(),
        "datasets": [
            {"name": "CycloneShield sample track", "status": "loaded", "license": "Project demo data"},
            {"name": "Regional exposure indices", "status": "loaded", "license": "Project demo data"},
            {"name": "Official forecast adapter", "status": "not configured", "license": "Provider terms required"},
        ],
        "limitations": [
            "No official live weather or shelter feed is active in this package.",
            "Use the demo indicators for presentation and engineering validation only.",
        ],
    }


@router.get("/model/metrics", response_model=ModelMetrics)
def model_metrics() -> dict:
    return {
        "mode": "RULE_BASED_FALLBACK",
        "task": "Interpretable regional exposure prioritization",
        "baseline": "Weighted transparent heuristic; no trained operational forecast model",
        "metrics": {"MAE": "N/A", "RMSE": "N/A", "calibration": "N/A"},
        "note": "A trained model is intentionally not claimed because this package does not ship a validated historical training dataset. Replace this adapter with a time-split evaluated model before operational use.",
    }
