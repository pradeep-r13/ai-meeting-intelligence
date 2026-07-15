from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import get_session
from app.schemas.meeting import (
    MeetingCreate,
    MeetingUpdate,
    MeetingResponse
)

from app.services.meeting_service import (
    create_meeting,
    get_all_meetings,
    get_meeting,
    update_meeting,
    delete_meeting
)

router = APIRouter(
    prefix="/meetings",
    tags=["Meetings"]
)


@router.post(
    "/",
    response_model=MeetingResponse
)
async def create_new_meeting(
    meeting: MeetingCreate,
    db: AsyncSession = Depends(get_session)
):

    return await create_meeting(
        meeting,
        db
    )


@router.get(
    "/",
    response_model=list[MeetingResponse]
)
async def read_meetings(
    db: AsyncSession = Depends(get_session)
):

    return await get_all_meetings(
        db
    )


@router.get(
    "/{meeting_id}",
    response_model=MeetingResponse
)
async def read_meeting(
    meeting_id: UUID,
    db: AsyncSession = Depends(get_session)
):

    return await get_meeting(
        meeting_id,
        db
    )


@router.put(
    "/{meeting_id}",
    response_model=MeetingResponse
)
async def edit_meeting(
    meeting_id: UUID,
    meeting: MeetingUpdate,
    db: AsyncSession = Depends(get_session)
):

    return await update_meeting(
        meeting_id,
        meeting,
        db
    )


@router.delete(
    "/{meeting_id}"
)
async def remove_meeting(
    meeting_id: UUID,
    db: AsyncSession = Depends(get_session)
):

    return await delete_meeting(
        meeting_id,
        db
    )
