from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.connection import get_session

from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
    TaskResponse
)

from app.services.task_service import (
    create_task,
    get_all_tasks,
    get_task,
    update_task,
    delete_task
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


@router.post(
    "/",
    response_model=TaskResponse
)
async def create_new_task(
    task: TaskCreate,
    db: AsyncSession = Depends(get_session)
):

    return await create_task(
        task,
        db
    )


@router.get(
    "/",
    response_model=list[TaskResponse]
)
async def read_tasks(
    db: AsyncSession = Depends(get_session)
):

    return await get_all_tasks(db)


@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
async def read_task(
    task_id: UUID,
    db: AsyncSession = Depends(get_session)
):

    return await get_task(
        task_id,
        db
    )


@router.put(
    "/{task_id}",
    response_model=TaskResponse
)
async def edit_task(
    task_id: UUID,
    task: TaskUpdate,
    db: AsyncSession = Depends(get_session)
):

    return await update_task(
        task_id,
        task,
        db
    )


@router.delete(
    "/{task_id}"
)
async def remove_task(
    task_id: UUID,
    db: AsyncSession = Depends(get_session)
):

    return await delete_task(
        task_id,
        db
    )
