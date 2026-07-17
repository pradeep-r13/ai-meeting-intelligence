from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.task import Task
from app.schemas.task import (
    TaskCreate,
    TaskUpdate
)


async def create_task(
    task: TaskCreate,
    db: AsyncSession
):

    new_task = Task(
        **task.model_dump()
    )

    db.add(new_task)

    await db.commit()

    await db.refresh(new_task)

    return new_task


async def get_all_tasks(
    db: AsyncSession
):

    result = await db.execute(
        select(Task)
    )

    return result.scalars().all()


async def get_task(
    task_id: UUID,
    db: AsyncSession
):

    result = await db.execute(
        select(Task).where(
            Task.id == task_id
        )
    )

    task = result.scalar_one_or_none()

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


async def update_task(
    task_id: UUID,
    task_data: TaskUpdate,
    db: AsyncSession
):

    task = await get_task(
        task_id,
        db
    )

    update_data = task_data.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(
            task,
            key,
            value
        )

    await db.commit()

    await db.refresh(task)

    return task


async def delete_task(
    task_id: UUID,
    db: AsyncSession
):

    task = await get_task(
        task_id,
        db
    )

    await db.delete(task)

    await db.commit()

    return {
        "message": "Task deleted successfully"
    }
