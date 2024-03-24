from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from users.dependencies import get_auth_username
from . import crud
from .dependencies import project_by_id
from .schemas import Project, ProjectCreate, ProjectUpdatePartial

router = APIRouter(tags=["Project"])


@router.get("/", response_model=list[Project])
async def get_projects(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.get_projects(session=session)


@router.post(
    "/",
    response_model=Project,
    status_code=status.HTTP_201_CREATED,
)
async def create_product(
    project_in: ProjectCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
    auth_user: AsyncSession = Depends(get_auth_username),
):
    if not auth_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not have permission",
        )
    project_in.user_id = auth_user.id
    return await crud.create_project(session=session, project_in=project_in)


@router.get("/{project_id}/", response_model=Project)
async def get_project(project: Project = Depends(project_by_id)):
    return project


@router.patch("/{project_id}/", response_model=Project)
async def update_project(
    project_update: ProjectUpdatePartial,
    project: Project = Depends(project_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
    auth_user: AsyncSession = Depends(get_auth_username),
):
    if not auth_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not have permission",
        )
    project.user_id = auth_user.id
    return await crud.update_project_partial(
        session=session,
        project=project,
        project_update=project_update,
    )


@router.delete(
    "/{project_id}/",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_project(
    project: Project = Depends(project_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
    auth_user: AsyncSession = Depends(get_auth_username),
):
    if not auth_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not have permission",
        )
    await crud.delete_project(session=session, project=project)
