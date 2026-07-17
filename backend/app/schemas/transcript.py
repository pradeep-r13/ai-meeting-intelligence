from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class TranscriptCreate(BaseModel):
    meeting_id: UUID
    speaker: str
    content: str
    start_time: float
    end_time: float


class TranscriptUpdate(BaseModel):
    speaker: str | None = None
    content: str | None = None
    start_time: float | None = None
    end_time: float | None = None


class TranscriptResponse(BaseModel):
    id: UUID
    meeting_id: UUID
    speaker: str
    content: str
    start_time: float
    end_time: float
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
