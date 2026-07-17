from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import get_session

from app.schemas.transcript import (
    TranscriptCreate,
    TranscriptUpdate,
    TranscriptResponse
)

from app.services.transcript_service import (
    create_transcript,
    get_all_transcripts,
    get_transcript,
    update_transcript,
    delete_transcript
)

router = APIRouter(
    prefix="/transcripts",
    tags=["Transcripts"]
)


@router.post(
    "/",
    response_model=TranscriptResponse
)
async def create_new_transcript(
    transcript: TranscriptCreate,
    db: AsyncSession = Depends(get_session)
):

    return await create_transcript(
        transcript,
        db
    )


@router.get(
    "/",
    response_model=list[TranscriptResponse]
)
async def read_transcripts(
    db: AsyncSession = Depends(get_session)
):

    return await get_all_transcripts(
        db
    )


@router.get(
    "/{transcript_id}",
    response_model=TranscriptResponse
)
async def read_transcript(
    transcript_id: UUID,
    db: AsyncSession = Depends(get_session)
):

    return await get_transcript(
        transcript_id,
        db
    )


@router.put(
    "/{transcript_id}",
    response_model=TranscriptResponse
)
async def edit_transcript(
    transcript_id: UUID,
    transcript: TranscriptUpdate,
    db: AsyncSession = Depends(get_session)
):

    return await update_transcript(
        transcript_id,
        transcript,
        db
    )


@router.delete(
    "/{transcript_id}"
)
async def remove_transcript(
    transcript_id: UUID,
    db: AsyncSession = Depends(get_session)
):

    return await delete_transcript(
        transcript_id,
        db
    )
