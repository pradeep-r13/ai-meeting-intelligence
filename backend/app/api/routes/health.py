from fastapi import APIRouter
from datetime import datetime, timezone

router = APIRouter()


@router.get('/health')
async def health_check():

    return {
        'status': 'healthy',
        'service': 'AI Meeting Intelligence API',
        'timestamp': datetime.now(timezone.utc)
    }
