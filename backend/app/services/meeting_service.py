from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.meeting import Meeting
from app.schemas.meeting import (
    MeetingCreate,
    MeetingUpdate
)


async def create_meeting(
    meeting: MeetingCreate,
    db: AsyncSession
):

    new_meeting = Meeting(
        **meeting.model_dump()
    )

    db.add(new_meeting)

    await db.commit()

    await db.refresh(new_meeting)

    return new_meeting


async def get_all_meetings(
    db: AsyncSession
):

    result = await db.execute(
        select(Meeting)
    )

    return result.scalars().all()


async def get_meeting(
    meeting_id: UUID,
    db: AsyncSession
):

    result = await db.execute(
        select(Meeting).where(
            Meeting.id == meeting_id
        )
    )

    meeting = result.scalar_one_or_none()

    if meeting is None:
        raise HTTPException(
            status_code=404,
            detail="Meeting not found"
        )

    return meeting


async def update_meeting(
    meeting_id: UUID,
    meeting_data: MeetingUpdate,
    db: AsyncSession
):

    meeting = await get_meeting(
        meeting_id,
        db
    )

    update_data = meeting_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            meeting,
            key,
            value
        )

    await db.commit()

    await db.refresh(meeting)

    return meeting


async def delete_meeting(
    meeting_id: UUID,
    db: AsyncSession
):

    meeting = await get_meeting(
        meeting_id,
        db
    )

    await db.delete(meeting)

    await db.commit()

    return {
        "message": "Meeting deleted successfully"
    }
