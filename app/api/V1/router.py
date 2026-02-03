from fastapi import APIRouter
from app.api.V1.endpoints import health

api_router = APIRouter(prefix="/api/v1")
api_router.include_router(health.router, tags=["health"])
