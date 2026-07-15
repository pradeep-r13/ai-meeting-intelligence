from datetime import datetime, timezone
from turtle import title
from uuid import UUID, uuid4
from venv import create

from sqlalchemy import (
    Text,
    String,
    DateTime,
    Float,
    ForeignKey
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.models import meeting


class Decision(Base):

    __tablename__ = 'decisions'

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
        index=True
    )

    meeting_id: Mapped[UUID] = mapped_column(
        ForeignKey('meetings.id'),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    confidence_score: Mapped[Float] = mapped_column(
        Float,
        default=0.0
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    # Relationship with meeting

    meeting = relationship(
        "Meeting",
        back_populates="decisions"
    )
