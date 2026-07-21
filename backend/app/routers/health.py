from fastapi import APIRouter

reouter = APIRouter()

@reouter.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}