from typing import List, Literal
from pydantic import BaseModel, Field


class Message(BaseModel):
    """
    PUBLIC_INTERFACE
    Represents a single message in the conversation.
    """
    role: Literal["user", "assistant"] = Field(..., description="Role of the message author.")
    content: str = Field(..., description="Message text content.")


class ChatRequest(BaseModel):
    """
    PUBLIC_INTERFACE
    Request body for the chat endpoint.
    """
    messages: List[Message] = Field(..., description="Ordered list of conversation messages.")


class ChatResponse(BaseModel):
    """
    PUBLIC_INTERFACE
    Response model for the chat endpoint.
    """
    reply: str = Field(..., description="Model generated reply.")
