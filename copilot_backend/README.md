# AI Copilot Backend (FastAPI)

FastAPI backend for the AI Copilot chat app. Provides:
- GET /api/health: Health check
- POST /api/chat: Send messages to Gemini and receive replies

## Setup

1) Create a virtual environment and install dependencies:
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
   pip install -r requirements.txt

2) Create .env from example and set your API key:
   cp .env.example .env
   # Edit .env and set GEMINI_API_KEY

3) Run the server (port 3001 recommended):
   uvicorn app.main:app --host 0.0.0.0 --port 3001 --reload

Docs: http://localhost:3001/docs

## Environment Variables

- GEMINI_API_KEY (required)
- GEMINI_MODEL (optional, default: gemini-1.5-flash)
- ALLOWED_ORIGINS (optional, default: http://localhost:3000)
- LOG_LEVEL (optional, default: INFO)
