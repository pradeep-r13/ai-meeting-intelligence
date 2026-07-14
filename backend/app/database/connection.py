from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker
)


from app.core.config import settings
from sqlalchemy.pool import NullPool

DATABASE_URL = (
    f"postgresql+asyncpg://"
    f"{settings.POSTGRES_USER}:"
    f"{settings.POSTGRES_PASSWORD}@"
    f"{settings.POSTGRES_HOST}:"
    f"{settings.POSTGRES_PORT}/"
    f"{settings.POSTGRES_DB}"
)

# Async Database Engine
engine = create_async_engine(
    url=DATABASE_URL,
    poolclass=NullPool,
    pool_pre_ping=True
)

# Async Session Factory
async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


# Dependency ke liye use hoga
async def get_session():

    async with async_session() as session:
        yield session
