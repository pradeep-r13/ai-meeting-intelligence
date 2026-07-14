from datetime import date, datetime, timezone
from uuid import UUID, uuid4

from sqlalchemy import (
    Text,
    String,
    Date,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Task(Base):

    __tablename__ = 'tasks'

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
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    assigned_to: Mapped[str] = mapped_column(
        String(100),
        nullable=True
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default='pending'
    )

    priority: Mapped[str] = mapped_column(
        String(50),
        default='medium'
    )

    due_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        default=datetime.now
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=False),
        default=datetime.now,
        onupdate=datetime.now
    )

    # Relationshipe with Meeting
    meeting = relationship(
        'Meeting',
        back_populates='tasks'
    )
