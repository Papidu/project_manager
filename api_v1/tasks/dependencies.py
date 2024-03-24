from typing import Annotated

from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.tasks import crud
from core.models import db_helper, Task


async def task_by_id(
    task_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Task:
    task = await crud.get_task(session=session, task_id=task_id)
    if task is not None:
        return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Project {task_id} not found. Check project_id.",
    )