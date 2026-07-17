from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import get_session

from app.schemas.decision import (
    DecisionCreate,
    DecisionUpdate,
    DecisionResponse
)

from app.services.decision_service import (
    create_decision,
    get_all_decisions,
    get_decision,
    update_decision,
    delete_decision
)

router = APIRouter(
    prefix="/decisions",
    tags=["Decisions"]
)


@router.post(
    "/",
    response_model=DecisionResponse
)
async def create_new_decision(
    decision: DecisionCreate,
    db: AsyncSession = Depends(get_session)
):

    return await create_decision(
        decision,
        db
    )


@router.get(
    "/",
    response_model=list[DecisionResponse]
)
async def read_decisions(
    db: AsyncSession = Depends(get_session)
):

    return await get_all_decisions(
        db
    )


@router.get(
    "/{decision_id}",
    response_model=DecisionResponse
)
async def read_decision(
    decision_id: UUID,
    db: AsyncSession = Depends(get_session)
):

    return await get_decision(
        decision_id,
        db
    )


@router.put(
    "/{decision_id}",
    response_model=DecisionResponse
)
async def edit_decision(
    decision_id: UUID,
    decision: DecisionUpdate,
    db: AsyncSession = Depends(get_session)
):

    return await update_decision(
        decision_id,
        decision,
        db
    )


@router.delete(
    "/{decision_id}"
)
async def remove_decision(
    decision_id: UUID,
    db: AsyncSession = Depends(get_session)
):

    return await delete_decision(
        decision_id,
        db
    )
