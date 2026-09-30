from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json()["mode"] == "DEMO"


def test_cyclone_is_explicitly_demo() -> None:
    response = client.get("/api/cyclones")
    assert response.status_code == 200
    assert response.json()[0]["data_mode"] == "DEMO"
    assert "not an official" in response.json()[0]["forecast_note"].lower()


def test_risk_has_exposure_boundary() -> None:
    response = client.get("/api/risk?region=kakinada")
    assert response.status_code == 200
    payload = response.json()
    assert payload["exposure_not_damage"] is True
    assert payload["risk_level"] in {"LOW", "MEDIUM", "HIGH", "CRITICAL"}
    assert payload["factors"]


def test_invalid_region_is_rejected() -> None:
    response = client.get("/api/risk?region=not-a-region")
    assert response.status_code == 404


def test_resource_filters_keep_demo_provenance() -> None:
    response = client.get("/api/resources?resource_type=Shelter")
    assert response.status_code == 200
    assert response.json()[0]["data_mode"] == "DEMO"


def test_preparedness_contains_accessibility_guidance() -> None:
    response = client.get("/api/preparedness?region=Kakinada%20Coast")
    assert response.status_code == 200
    assert "Accessibility" in response.json()["guidance"]
