from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database.models.user import User
from app.schemas.user import (
    UserCreate,
    UserUpdate
)


async def create_user(
    db: AsyncSession,
    user_data: UserCreate
):

    user = User(
        email=user_data.email,
        full_name=user_data.full_name,
        hashed_password=user_data.password
    )

    db.add(user)

    await db.commit()

    await db.refresh(user)

    return user


async def get_users(
        db: AsyncSession
):

    result = await db.execute(
        select(User)
    )

    return result.scalars().all()

# Get User By ID


async def get_user_by_id(
    db: AsyncSession,
    user_id: UUID
):

    result = await db.execute(
        select(User)
        .where(User.id == user_id)
    )

    return result.scalar_one_or_none()

# Update User


async def update_user(
    db: AsyncSession,
    user_id: UUID,
    user_data: UserUpdate
):

    user = await get_user_by_id(
        db,
        user_id
    )

    if not user:
        return None

    if user_data.email:
        user.email = user_data.email

    if user_data.full_name:
        user.full_name = user_data.full_name

    await db.commit()

    await db.refresh(user)

    return user


# Delete User
async def delete_user(
    db: AsyncSession,
    user_id: UUID
):

    user = await get_user_by_id(
        db,
        user_id
    )

    if not user:
        return False

    await db.delete(user)

    await db.commit()

    return True
