from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.transcript import Transcript
from app.schemas.transcript import (
    TranscriptCreate,
    TranscriptUpdate
)


async def create_transcript(
    transcript: TranscriptCreate,
    db: AsyncSession
):

    new_transcript = Transcript(
        **transcript.model_dump()
    )

    db.add(new_transcript)

    await db.commit()

    await db.refresh(new_transcript)

    return new_transcript


async def get_all_transcripts(
    db: AsyncSession
):

    result = await db.execute(
        select(Transcript)
    )

    return result.scalars().all()


async def get_transcript(
    transcript_id: UUID,
    db: AsyncSession
):

    result = await db.execute(
        select(Transcript).where(
            Transcript.id == transcript_id
        )
    )

    transcript = result.scalar_one_or_none()

    if transcript is None:
        raise HTTPException(
            status_code=404,
            detail="Transcript not found"
        )

    return transcript


async def update_transcript(
    transcript_id: UUID,
    transcript_data: TranscriptUpdate,
    db: AsyncSession
):

    transcript = await get_transcript(
        transcript_id,
        db
    )

    update_data = transcript_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            transcript,
            key,
            value
        )

    await db.commit()

    await db.refresh(transcript)

    return transcript


async def delete_transcript(
    transcript_id: UUID,
    db: AsyncSession
):

    transcript = await get_transcript(
        transcript_id,
        db
    )

    await db.delete(transcript)

    await db.commit()

    return {
        "message": "Transcript deleted successfully"
    }
