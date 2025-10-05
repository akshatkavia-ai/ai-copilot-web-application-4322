import logging
import os
from contextlib import asynccontextmanager
from typing import List

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.routers.health import router as health_router
from app.routers.chat import router as chat_router

# Load environment variables from .env if present
load_dotenv()

# Configure logging
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO"),
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("copilot_backend")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown hooks."""
    logger.info("Starting AI Copilot backend...")
    yield
    logger.info("Shutting down AI Copilot backend...")


def _get_allowed_origins() -> List[str]:
    # Default to React dev server
    default = ["http://localhost:3000"]
    env_val = os.getenv("ALLOWED_ORIGINS")
    if not env_val:
        return default
    # Comma separated list from env
    origins = [o.strip() for o in env_val.split(",") if o.strip()]
    return origins or default


# Initialize FastAPI with metadata for OpenAPI/Swagger
app = FastAPI(
    title="AI Copilot Backend",
    description="FastAPI backend for AI Copilot chat app integrating Google Gemini.",
    version="0.1.0",
    lifespan=lifespan,
    openapi_tags=[
        {"name": "Health", "description": "Service health endpoints"},
        {"name": "Chat", "description": "Chat with the AI Copilot (Gemini)"},
    ],
)

# CORS config to allow frontend localhost by default
app.add_middleware(
    CORSMiddleware,
    allow_origins=_get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(health_router, prefix="/api", tags=["Health"])
app.include_router(chat_router, prefix="/api", tags=["Chat"])


@app.get(
    "/api/websocket-info",
    tags=["Health"],
    summary="WebSocket usage note",
    description="This project does not expose WebSocket endpoints yet. Real-time features may be added later.",
)
def websocket_info():
    """
    PUBLIC_INTERFACE
    Returns a note about WebSocket usage for this project.

    Returns:
        JSONResponse: Simple informational message.
    """
    return JSONResponse({"message": "No WebSocket endpoints available at the moment."})
