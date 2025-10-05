from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()


@router.get(
    "/health",
    summary="Health check",
    description="Returns a simple OK status to verify the service is running.",
    responses={
        200: {
            "description": "Service is healthy",
            "content": {"application/json": {"example": {"status": "ok"}}},
        }
    },
)
def health_check():
    """
    PUBLIC_INTERFACE
    Health check endpoint.

    Returns:
        JSONResponse: {'status': 'ok'} when the service is running.
    """
    return JSONResponse({"status": "ok"})
