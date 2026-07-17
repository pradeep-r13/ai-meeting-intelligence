from datetime import datetime
from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator
)


class TaskCreate(BaseModel):

    meeting_id: UUID

    title: str = Field(
        ...,
        min_length=3,
        max_length=255
    )

    description: str | None = Field(
        default=None,
        max_length=2000
    )

    assigned_to: str | None = Field(
        default=None,
        max_length=255
    )

    due_date: datetime | None = None

    priority: str = Field(
        default="medium"
    )

    status: str = Field(
        default="pending"
    )

    @field_validator("priority")
    @classmethod
    def validate_priority(cls, value: str):

        allowed = {
            "low",
            "medium",
            "high"
        }

        value = value.lower()

        if value not in allowed:
            raise ValueError(
                "Priority must be low, medium or high."
            )

        return value

    @field_validator("status")
    @classmethod
    def validate_status(cls, value: str):

        allowed = {
            "pending",
            "in_progress",
            "completed"
        }

        value = value.lower()

        if value not in allowed:
            raise ValueError(
                "Status must be pending, in_progress or completed."
            )

        return value


class TaskUpdate(BaseModel):

    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=255
    )

    description: str | None = Field(
        default=None,
        max_length=2000
    )

    assigned_to: str | None = Field(
        default=None,
        max_length=255
    )

    due_date: datetime | None = None

    priority: str | None = None

    status: str | None = None

    @field_validator("priority")
    @classmethod
    def validate_priority(cls, value):

        if value is None:
            return value

        allowed = {
            "low",
            "medium",
            "high"
        }

        value = value.lower()

        if value not in allowed:
            raise ValueError(
                "Priority must be low, medium or high."
            )

        return value

    @field_validator("status")
    @classmethod
    def validate_status(cls, value):

        if value is None:
            return value

        allowed = {
            "pending",
            "in_progress",
            "completed"
        }

        value = value.lower()

        if value not in allowed:
            raise ValueError(
                "Status must be pending, in_progress or completed."
            )

        return value


class TaskResponse(BaseModel):

    id: UUID

    meeting_id: UUID

    title: str

    description: str | None

    assigned_to: str | None

    due_date: datetime | None

    priority: str

    status: str

    created_at: datetime

    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
