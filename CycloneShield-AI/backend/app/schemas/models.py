from typing import Literal

from pydantic import BaseModel, Field


Severity = Literal["LOW", "MEDIUM", "HIGH", "CRITICAL"]


class TrackPoint(BaseModel):
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    timestamp: str
    wind_speed_kmh: float = Field(ge=0)


class CycloneSummary(BaseModel):
    id: str
    name: str
    status: str
    data_mode: Literal["DEMO", "LIVE", "MODEL_ESTIMATE"]
    source: str
    last_updated: str
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    wind_speed_kmh: float = Field(ge=0)
    pressure_hpa: float = Field(ge=800, le=1100)
    movement: str
    track: list[TrackPoint]
    forecast_track: list[TrackPoint]
    forecast_note: str


class RiskFactor(BaseModel):
    name: str
    value: str
    contribution: float = Field(ge=0, le=100)
    available: bool = True
    explanation: str


class RiskResponse(BaseModel):
    region: str
    risk_score: float = Field(ge=0, le=100)
    risk_level: Severity
    exposure_not_damage: bool = True
    data_mode: Literal["DEMO", "LIVE", "MODEL_ESTIMATE"]
    factors: list[RiskFactor]
    limitations: list[str]
    last_updated: str


class PreparednessResponse(BaseModel):
    region: str
    data_mode: Literal["DEMO", "LIVE", "MODEL_ESTIMATE"]
    guidance: dict[str, list[str]]
    emergency_note: str
    limitations: list[str]


class Resource(BaseModel):
    id: str
    name: str
    resource_type: Literal["Shelter", "Hospital", "Emergency Service", "Relief Point"]
    region: str
    latitude: float = Field(ge=-90, le=90)
    longitude: float = Field(ge=-180, le=180)
    status: str
    contact: str
    data_mode: Literal["DEMO", "LIVE", "MODEL_ESTIMATE"]
    verification_note: str


class DataStatus(BaseModel):
    mode: Literal["DEMO", "LIVE", "MODEL_ESTIMATE"]
    live_provider: str
    live_available: bool
    last_checked: str
    datasets: list[dict[str, str]]
    limitations: list[str]


class ModelMetrics(BaseModel):
    mode: str
    task: str
    baseline: str
    metrics: dict[str, float | str]
    note: str
