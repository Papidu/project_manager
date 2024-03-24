from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from users.dependencies import get_auth_username
from . import crud
from .dependencies import task_by_id
from .schemas import Task, TaskCreate, TaskUpdatePartial

router = APIRouter(tags=["Task"])


@router.get("/", response_model=list[Task])
async def get_projects(
    session: AsyncSession = Depends(db_helper.session_dependency),
    auth_user: AsyncSession = Depends(get_auth_username),
):
    return await crud.get_tasks(session=session)


@router.post(
    "/",
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
)
async def create_task(
    task_in: TaskCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
    auth_user: AsyncSession = Depends(get_auth_username),
):
    return await crud.create_project(session=session, task_in=task_in)


@router.get("/{task_id}/", response_model=Task)
async def get_task(
    task: Task = Depends(task_by_id),
    auth_user: AsyncSession = Depends(get_auth_username),
):
    return task


@router.patch("/{task_id}/", response_model=Task)
async def update_project(
    task_update: TaskUpdatePartial,
    task: Task = Depends(task_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
    auth_user: AsyncSession = Depends(get_auth_username),
):
    return await crud.update_task_partial(
        session=session,
        task=task,
        task_update=task_update,
    )


@router.delete(
    "/{project_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_project(
    task: Task = Depends(task_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
    auth_user: AsyncSession = Depends(get_auth_username),
) -> None:
    if auth_user.id == task.user_id or auth_user.is_admin:
        await crud.delete_project(session=session, task=task)

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Not have permission",
    )