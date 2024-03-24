from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import ProjectCreate, ProjectUpdatePartial
from core.models import Project


async def get_projects(session: AsyncSession) -> list[Project]:
    stmt = select(Project)
    result: Result = await session.execute(stmt)
    projects = result.scalars().all()
    return list(projects)


async def get_project(session: AsyncSession, project_id: int) -> Project | None:
    return await session.get(Project, project_id)


async def create_project(session: AsyncSession, project_in: ProjectCreate) -> Project:
    project = Project(**project_in.model_dump())
    session.add(project)
    await session.commit()
    await session.refresh(project)
    return project


async def update_project_partial(
    session: AsyncSession,
    project: Project,
    project_update: ProjectUpdatePartial,
) -> Project:
    for key, value in project_update.model_dump(exclude_unset=True).items():
        setattr(project, key, value)
    await session.commit()
    return project


async def delete_project(session: AsyncSession, project: Project) -> None:
    await session.delete(project)
    await session.commit()