from fastapi import APIRouter, FastAPI
from fastapi.routing import APIRoute

from app.core.logging import logger


router = APIRouter()


@router.get('/health')
def health_check():

    logger.info('Health check API called')

    return {
        'status': 'healthy',
        'service': 'backend'
    }
