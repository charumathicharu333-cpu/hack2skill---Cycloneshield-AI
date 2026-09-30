# hack2skill-Track-5-Cyclone-Impact-Infrastructure-Vulnerability-Forecaster

# 🌪️ CycloneShield AI

### AI-Powered Cyclone Intelligence, Risk Assessment & Disaster Preparedness Platform

> **Smarter Cyclone Intelligence • Safer Communities • Better Preparedness**
---
**prototype link** : https://cycloneshield-ai-rzog.onrender.com
---

## 📌 Overview

**CycloneShield AI** is an AI-powered disaster preparedness platform designed to help communities understand cyclone-related risks and make better-informed preparedness decisions.

The platform combines **weather information, cyclone tracking, geographic risk analysis, machine learning, and intelligent preparedness recommendations** into a single interactive dashboard.

CycloneShield AI is designed as a hackathon prototype with a strong focus on **AI-assisted decision support, explainability, accessibility, and disaster resilience**.

---

## 🎯 Problem Statement

Cyclones can cause severe impacts through:

* 🌪️ High-speed winds
* 🌧️ Heavy rainfall
* 🌊 Coastal flooding
* 🏠 Infrastructure damage
* 🚨 Evacuation challenges
* 👨‍👩‍👧‍👦 Community safety risks

People often receive information from multiple sources, making it difficult to understand **what the potential risk means for their specific region**.

CycloneShield AI aims to bring relevant information together into an easy-to-understand platform.

---

## 💡 Our Solution

CycloneShield AI provides a centralized platform for:

**Weather Data → AI Analysis → Risk Assessment → Visualization → Preparedness Guidance**

The system can analyze available cyclone and geographic information and present the results through an interactive dashboard.

---

## 🚀 Key Features

### 🌪️ 1. Cyclone Intelligence

* Cyclone location visualization
* Wind-speed information
* Pressure information when available
* Movement direction
* Observation timestamp
* Data-source identification

---

### 🗺️ 2. Interactive Cyclone Tracker

The map can display:

* Cyclone position
* Historical track
* Available forecast information
* Geographic regions
* Risk zones
* Relevant resources

> Forecast information is clearly distinguished from simulated or demonstration data.

---

### ⚠️ 3. Regional Risk Assessment

Users can select a location or region and view available risk indicators.

The system can consider factors such as:

* Wind
* Rainfall
* Geographic exposure
* Population exposure
* Elevation
* Coastal proximity
* Available cyclone information

The resulting risk assessment is designed to be **interpretable rather than a black-box score**.

---

### 🤖 4. AI / Machine Learning

CycloneShield AI supports machine-learning-based analysis where suitable historical data is available.

Possible ML tasks include:

* Cyclone intensity analysis
* Historical pattern analysis
* Hazard classification
* Risk estimation
* Anomaly detection

The project compares model results against appropriate baselines and reports evaluation metrics.

---

### 🧠 5. Explainable Risk Analysis

Instead of showing only a risk value, the dashboard explains the factors contributing to the assessment.

Example:

```text
Regional Risk Assessment

Wind Exposure       ████████░░  High
Rainfall Exposure   ██████░░░░  Moderate
Coastal Exposure    █████████░  High
Population Exposure ███████░░░  Moderate
```

This makes the system easier for non-technical users to understand.

---

### 🛡️ 6. Smart Preparedness Recommendations

The platform provides preparedness guidance based on available hazard information.

Examples include:

* Emergency-kit preparation
* Important document protection
* Safe shelter preparation
* Evacuation-readiness guidance
* Communication planning
* Emergency contact preparation

Recommendations are presented as **decision-support information**, not as replacements for official emergency instructions.

---

### 🏥 7. Shelter & Emergency Resources

Where verified data is available, users can explore:

* Emergency shelters
* Hospitals
* Emergency services
* Evacuation resources
* Important contact information

Demo resources are explicitly labelled as **DEMO DATA**.

---

### 📊 8. AI Dashboard

The dashboard provides:

* Cyclone status
* Risk indicators
* Interactive maps
* Charts
* Historical information
* Model information
* Data-source status
* Preparedness recommendations

---

## 🏗️ System Architecture

```text
                 ┌─────────────────────┐
                 │  Public Data Sources │
                 │ Weather / Historical│
                 │ Geographic Data     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Data Processing   │
                 │ Cleaning & Feature  │
                 │ Engineering         │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ AI / ML Analysis    │
                 │ Risk Estimation     │
                 │ Pattern Analysis    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   FastAPI Backend   │
                 │ REST APIs            │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ React Frontend      │
                 │ Dashboard + Map     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │     End Users       │
                 │ Residents / Teams   │
                 └─────────────────────┘
```

---

## 🧰 Technology Stack

### Frontend

* React
* Vite
* JavaScript / TypeScript
* Leaflet
* Chart.js / Recharts
* Responsive CSS

### Backend

* Python
* FastAPI
* Pydantic
* Pandas
* NumPy

### AI / ML

* Scikit-learn
* Feature engineering
* Statistical analysis
* Explainable risk estimation

### Database / Storage

* CSV / Parquet
* SQLite where required

### Testing

* Pytest
* API testing
* Integration testing

---

## 📁 Project Structure

```text
CycloneShield-AI/
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── hooks/
│   │   └── styles/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   │
│   ├── tests/
│   └── requirements.txt
│
├── data/
│   ├── sample/
│   ├── processed/
│   └── README.md
│
├── ml/
│   ├── training/
│   ├── evaluation/
│   └── artifacts/
│
├── docs/
│   ├── architecture.md
│   ├── data_sources.md
│   ├── model_card.md
│   └── demo_script.md
│
├── scripts/
│
├── .env.example
├── .gitignore
├── README.md
├── start_windows.bat
└── start_unix.sh
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CycloneShield-AI.git
cd CycloneShield-AI
```

---

### 2. Backend Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
cd backend
pip install -r requirements.txt
```

---

### 3. Start Backend

```bash
uvicorn app.main:app --reload
```

Backend:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

### 4. Frontend Setup

Open another terminal:

```bash
cd frontend
npm install
npm run dev
```

Frontend:

```text
http://localhost:5173
```

---

## 🔌 API Endpoints

| Endpoint             | Purpose                      |
| -------------------- | ---------------------------- |
| `/api/health`        | Backend health check         |
| `/api/cyclones`      | Cyclone information          |
| `/api/cyclones/{id}` | Specific cyclone             |
| `/api/risk`          | Regional risk assessment     |
| `/api/preparedness`  | Preparedness recommendations |
| `/api/resources`     | Emergency resources          |
| `/api/data-status`   | Data-source status           |
| `/api/model/metrics` | ML evaluation information    |

---

## 📊 Model Evaluation

CycloneShield AI should report actual evaluation results for the selected ML task.

Example metrics:

```text
MAE
RMSE
Precision
Recall
F1 Score
```

The project does **not** claim operational forecasting accuracy unless independently validated against appropriate historical or real-world data.

---

## 🔐 Data & Safety

CycloneShield AI follows several important principles:

* No fabricated official warnings.
* No fabricated evacuation orders.
* No fake live cyclone information.
* Demo data is clearly labelled.
* Model estimates are distinguished from official forecasts.
* Data sources are documented.
* API keys are never committed to GitHub.
* Personal information is not included in the repository.

For real emergencies, users should follow instructions from relevant official disaster-management and meteorological authorities.

---

## 💻 Resource Efficiency

The project is designed to run on a normal student laptop.

Large datasets should be processed using:

* Chunked file processing
* Column selection
* Memory-efficient data types
* Incremental output
* Pagination
* Limited concurrent processing

The application should avoid loading unnecessarily large datasets entirely into RAM.

---

## 🧪 Testing

Run backend tests:

```bash
pytest
```

Run frontend checks:

```bash
npm run build
```

The project should verify:

* API availability
* Input validation
* Missing-data handling
* Invalid coordinates
* Empty datasets
* API failures
* Frontend/backend integration

---

## 🎥 Demo Flow

The recommended hackathon demonstration is:

```text
1. Open CycloneShield AI
        ↓
2. View cyclone dashboard
        ↓
3. Open interactive map
        ↓
4. Select a region
        ↓
5. View regional risk factors
        ↓
6. Explore AI analysis
        ↓
7. Generate preparedness guidance
        ↓
8. Explore available resources
        ↓
9. View model/data transparency
```

---

## 🌟 Innovation

CycloneShield AI focuses on combining multiple capabilities into one decision-support platform:

```text
Cyclone Intelligence
        +
Geospatial Visualization
        +
AI / ML Analysis
        +
Regional Risk Assessment
        +
Explainability
        +
Preparedness Guidance
        =
CycloneShield AI
```

The goal is not simply to display cyclone information, but to make complex information easier to understand and act upon.

---

## 🔮 Future Scope

Potential future improvements include:

* Real-time satellite-data integration
* Improved cyclone intensity modelling
* Flood-depth estimation
* Hyperlocal rainfall prediction
* Multilingual voice assistance
* SMS-based alerts
* Offline emergency mode
* Community reporting
* IoT weather-station integration
* Advanced geospatial modelling
* Mobile application
* Accessibility-focused interfaces

---

**CycloneShield AI**

Developed as an AI-powered disaster resilience and preparedness hackathon project.

---


## ⭐ Project Vision

> **From cyclone data to understandable risk insights — helping communities prepare before disaster strikes.**

---

## 📄 License

Add the license selected by the project team before publishing the repository.
