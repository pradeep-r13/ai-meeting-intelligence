from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class DecisionCreate(BaseModel):

    meeting_id: UUID

    title: str = Field(
        ...,
        min_length=3,
        max_length=255
    )

    description: str = Field(
        ...,
        min_length=3
    )

    decision_by: str | None = Field(
        default=None,
        max_length=255
    )

    priority: str = Field(
        default="medium"
    )

    status: str = Field(
        default="pending"
    )


class DecisionUpdate(BaseModel):

    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=255
    )

    description: str | None = Field(
        default=None,
        min_length=3
    )

    decision_by: str | None = Field(
        default=None,
        max_length=255
    )

    priority: str | None = None

    status: str | None = None


class DecisionResponse(BaseModel):

    id: UUID
    meeting_id: UUID

    title: str
    description: str

    decision_by: str | None

    priority: str
    status: str

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
