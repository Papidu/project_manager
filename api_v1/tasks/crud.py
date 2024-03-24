from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import TaskCreate, TaskUpdatePartial
from core.models import Task


async def get_tasks(
    session: AsyncSession,
) -> list[Task]:
    stmt = select(Task)
    result: Result = await session.execute(stmt)
    task = result.scalars().all()
    return list(task)


async def get_task(session: AsyncSession, task_id: int) -> Task | None:
    return await session.get(Task, task_id)


async def create_project(session: AsyncSession, task_in: TaskCreate) -> Task:
    task = Task(**task_in.model_dump())
    session.add(task)
    await session.commit()
    await session.refresh(task)
    return task


async def update_task_partial(
    session: AsyncSession,
    task: Task,
    task_update: TaskUpdatePartial,
) -> Task:
    for key, value in task_update.model_dump(exclude_unset=True).items():
        setattr(task, key, value)
    await session.commit()
    return task


async def delete_project(session: AsyncSession, task: Task) -> None:
    await session.delete(task)
    await session.commit()