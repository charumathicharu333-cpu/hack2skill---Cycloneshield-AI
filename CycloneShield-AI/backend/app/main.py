from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.api.routes import router

BASE_DIR = Path(__file__).resolve().parents[2]
FRONTEND_DIR = BASE_DIR / "frontend"

app = FastAPI(
    title="CycloneShield AI API",
    version="0.1.0",
    description="Local-first cyclone preparedness MVP with explicit demo-mode provenance.",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:8000"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)
app.include_router(router)


@app.get("/api/docs-note", include_in_schema=False)
def docs_note() -> dict:
    return {"message": "Interactive OpenAPI documentation is available at /docs"}


app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
