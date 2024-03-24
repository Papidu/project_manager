from typing import Annotated

from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.projects import crud
from core.models import db_helper, Project


async def project_by_id(
    project_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Project:
    project = await crud.get_project(session=session, project_id=project_id)
    if project is not None:
        return project

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Project {project_id} not found. Check project_id.",
    )
