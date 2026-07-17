from fastapi import FastAPI

from app.api.routes.users import router as users_router
from app.api.routes.meetings import router as meetings_router
from app.api.routes.transcripts import router as transcripts_router
from app.api.routes.decisions import router as decisions_router
from app.api.routes.tasks import router as tasks_router

app = FastAPI(
    title="AI Meeting Intelligence",
    version="1.0.0"
)

app.include_router(
    users_router,
    prefix="/api/v1"
)

app.include_router(
    meetings_router,
    prefix="/api/v1"
)

app.include_router(
    transcripts_router,
    prefix="/api/v1"
)

app.include_router(
    decisions_router,
    prefix="/api/v1"
)

app.include_router(
    tasks_router,
    prefix="/api/v1"
)


@app.get("/")
async def root():
    return {
        "message": "AI Meeting Intelligence API"
    }
