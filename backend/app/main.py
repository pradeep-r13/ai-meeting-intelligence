from fastapi import FastAPI

from backend.alembic.api.routes import health
from backend.alembic.api.routes import users

from app.core.logging import setup_logging, logger


setup_logging()


app = FastAPI(
    title='AI Meeting Intelligence & Decision Tracker',
    description='Enterprise AI meeting platform',
    version='1.0.0'
)

logger.info('AI Meeting Intelligence Backend Started ')


@app.get('/')
def root():
    return {
        'message': 'AI Meeting Intelligence Backend Running'
    }


app.include_router(
    router=health.router,
    prefix='',
    tags=['Health']
)


app.include_router(
    router=users.router,
    prefix='',
    tags=['Users']
)
