from fastapi import APIRouter

from app.api.routes import health
from app.api.routes import users

api_router = APIRouter()


api_router.include_router(
    router=health.router,
    tags=['Health']
)

api_router.include_router(
    router=users.router,
    tags=['Users']
)
