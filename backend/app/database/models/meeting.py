from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy import (
    String,
    Text,
    DateTime,
    ForeignKey,
)

from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database.base import Base

from app.database.models.user import User


class Meeting(Base):

    __tablename__ = "meetings"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    owner_id: Mapped[UUID] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
        index=True
    )

    status: Mapped[str] = mapped_column(
        String(255),
        default="created"
    )

    meeting_date: Mapped[datetime] = mapped_column(
        DateTime,
        default=timezone.utc
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=timezone.utc
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=timezone.utc,
        onupdate=timezone.utc
    )

    # Relationship with User

    owner = relationship(
        "User",
        back_populates="meetings"
    )

    transcripts = relationship(
        "Transcript",
        back_populates="meetings"
    )

    decisions = relationship(
        'Decision',
        back_populates='meetings'
    )
