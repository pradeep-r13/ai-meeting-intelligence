from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import get_db

from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserUpdate
)

from app.services.user_service import (
    create_user,
    get_users,
    get_user_by_id,
    update_user,
    delete_user
)


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# CREATE USER
@router.post(
    "/",
    response_model=UserResponse
)
async def create_new_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):

    return await create_user(
        db,
        user
    )


# GET ALL USERS
@router.get(
    "/",
    response_model=list[UserResponse]
)
async def list_users(
    db: AsyncSession = Depends(get_db)
):

    return await get_users(db)


# GET USER BY ID
@router.get(
    "/{user_id}",
    response_model=UserResponse
)
async def get_single_user(
    user_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    user = await get_user_by_id(
        db,
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# UPDATE USER
@router.put(
    "/{user_id}",
    response_model=UserResponse
)
async def update_existing_user(
    user_id: UUID,
    user_data: UserUpdate,
    db: AsyncSession = Depends(get_db)
):

    user = await update_user(
        db,
        user_id,
        user_data
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# DELETE USER
@router.delete(
    "/{user_id}"
)
async def remove_user(
    user_id: UUID,
    db: AsyncSession = Depends(get_db)
):

    deleted = await delete_user(
        db,
        user_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }
