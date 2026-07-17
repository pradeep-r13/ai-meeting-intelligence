from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.decision import Decision
from app.schemas.decision import (
    DecisionCreate,
    DecisionUpdate
)


async def create_decision(
    decision: DecisionCreate,
    db: AsyncSession
):

    new_decision = Decision(
        **decision.model_dump()
    )

    db.add(new_decision)

    await db.commit()

    await db.refresh(new_decision)

    return new_decision


async def get_all_decisions(
    db: AsyncSession
):

    result = await db.execute(
        select(Decision)
    )

    return result.scalars().all()


async def get_decision(
    decision_id: UUID,
    db: AsyncSession
):

    result = await db.execute(
        select(Decision).where(
            Decision.id == decision_id
        )
    )

    decision = result.scalar_one_or_none()

    if decision is None:
        raise HTTPException(
            status_code=404,
            detail="Decision not found"
        )

    return decision


async def update_decision(
    decision_id: UUID,
    decision_data: DecisionUpdate,
    db: AsyncSession
):

    decision = await get_decision(
        decision_id,
        db
    )

    update_data = decision_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            decision,
            key,
            value
        )

    await db.commit()

    await db.refresh(decision)

    return decision


async def delete_decision(
    decision_id: UUID,
    db: AsyncSession
):

    decision = await get_decision(
        decision_id,
        db
    )

    await db.delete(decision)

    await db.commit()

    return {
        "message": "Decision deleted successfully"
    }
