from datetime import datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy import (
    String,
    Text,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.database.base import Base


class Decision(Base):

    __tablename__ = "decisions"

    id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
        index=True
    )

    meeting_id: Mapped[UUID] = mapped_column(
        ForeignKey("meetings.id"),
        nullable=False,
        index=True
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    decision_by: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    priority: Mapped[str] = mapped_column(
        String(30),
        default="medium"
    )

    status: Mapped[str] = mapped_column(
        String(30),
        default="pending"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    meeting = relationship(
        "Meeting",
        back_populates="decisions"
    )
