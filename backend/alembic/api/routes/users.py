from fastapi import APIRouter
from app.core.logging import logger

router = APIRouter()


@router.get('/users')
def get_user():

    logger.info('Get User API called')

    return {
        'message': 'Users API working'
    }
