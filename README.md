# Cloud Recommendation Engine

A Python + React application that helps users describe their workload in natural language, extracts technical and compliance requirements, and recommends cloud services with price and feature comparison.

## Stack

- Frontend: React
- Backend: Python + FastAPI
- Database: PostgreSQL
- Storage: Azure Blob Storage
- AI: Azure OpenAI

## Local setup

1. Open the project root and ensure the existing .env file contains your Azure and database settings.
2. Create a virtual environment in the backend folder.
3. Install Python dependencies.
4. Start the backend.
5. Install frontend dependencies.
6. Start the frontend.

Example:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

In another terminal:

```bash
cd frontend
npm install
npm run dev
```

## Features

- natural-language requirement intake
- profile and user registration flow
- questionnaire for workload, usage, compliance, and specs
- AI-generated prompt and recommendation summary
- provider comparison across AWS, Azure, and GCP
- cost comparison table
- on-demand CSV and Excel table exports, interactive HTML reports, and formatted PDF reports
- saved search history
- security and audit logging design

CSV and Excel exports contain tabular recommendation data only. HTML and PDF exports include report narrative and recommendation tables.

## Notes

This scaffold is intentionally minimal but ready to extend with PostgreSQL persistence, document uploads, Azure Blob integration, and deeper AI orchestration.
