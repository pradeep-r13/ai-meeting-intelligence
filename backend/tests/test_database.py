import pytest

from sqlalchemy import text

from app.database.connection import engine


@pytest.mark.asyncio
async def test_database_connection():

    async with engine.begin() as conn:

        result = await conn.execute(
            text("SELECT 1")
        )

    assert result is not None
