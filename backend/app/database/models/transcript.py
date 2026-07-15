from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy import (
    String,
    Float,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Transcript(Base):

    __tablename__ = 'transcripts'

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

    speaker: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    timestamp: Mapped[str] = mapped_column(
        Float,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    meeting = relationship(
        'Meeting',
        back_populates='transcripts'
    )
