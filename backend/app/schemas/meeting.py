from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class MeetingCreate(BaseModel):
    title: str
    description: str | None = None
    owner_id: UUID
    meeting_date: datetime


class MeetingUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None
    meeting_date: datetime | None = None


class MeetingResponse(BaseModel):
    id: UUID
    title: str
    description: str | None
    owner_id: UUID
    status: str
    meeting_date: datetime
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
