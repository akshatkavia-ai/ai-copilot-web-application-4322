# AI Copilot Web Application

This repository contains the backend (FastAPI) for an AI Copilot application.
- Backend workspace: ai-copilot-web-application-4322/copilot_backend
- Frontend is in a separate workspace: ai-copilot-web-application-4324/copilot_frontend

Backend quick start:
1) cd ai-copilot-web-application-4322/copilot_backend
2) cp .env.example .env  # set GEMINI_API_KEY
3) pip install -r requirements.txt
4) uvicorn app.main:app --host 0.0.0.0 --port 3001 --reload

OpenAPI docs at http://localhost:3001/docs