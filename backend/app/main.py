from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.config import settings
from app.api.routes import health
from app.api.routes import users


@asynccontextmanager
async def lifespan(app: FastAPI):

    print(
        f"{settings.APP_NAME} started successfully"
    )

    yield

    print(
        "Application shutdown"
    )


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan
)


@app.get("/")
async def root():

    return {
        "message": "AI Meeting Intelligence API Running"
    }


app.include_router(
    health.router,
    prefix="/api/v1",
    tags=["Health"]
)


app.include_router(
    users.router,
    prefix="/api/v1/users",
    tags=["Users"]
)
