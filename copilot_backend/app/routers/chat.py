import logging
import os
from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from app.models.schemas import ChatRequest, ChatResponse
from app.services.gemini_client import GeminiClient, GeminiClientError

logger = logging.getLogger("copilot_backend.chat")

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse,
    summary="Chat with AI Copilot (Gemini)",
    description="Accepts a message history and returns a model-generated reply using Google Gemini.",
    responses={
        200: {
            "description": "AI response returned.",
            "content": {"application/json": {"example": {"reply": "Hello! How can I help you?"}}},
        },
        400: {"description": "Invalid input."},
        500: {"description": "Server error or missing API key."},
    },
)
def chat(req: ChatRequest):
    """
    PUBLIC_INTERFACE
    Chat endpoint that sends the provided conversation to Gemini and returns a reply.

    Args:
        req (ChatRequest): The chat request containing the message history.

    Returns:
        ChatResponse: The AI generated reply.

    Raises:
        HTTPException: 500 if GEMINI_API_KEY is missing or any server error occurs.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        logger.error("GEMINI_API_KEY is not set.")
        raise HTTPException(status_code=500, detail="GEMINI_API_KEY is not configured on the server.")
    model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

    client = GeminiClient(api_key=api_key, model_name=model_name)
    try:
        reply = client.generate_reply(req.messages)
        return JSONResponse(ChatResponse(reply=reply).model_dump())
    except GeminiClientError as ge:
        logger.exception("Gemini client error: %s", ge)
        raise HTTPException(status_code=500, detail=str(ge))
    except Exception as e:
        logger.exception("Unexpected server error: %s", e)
        raise HTTPException(status_code=500, detail="Unexpected server error")
