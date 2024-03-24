import asyncio
from typing import Literal

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, User, Project, Subproject, Task


async def create_user(
    session: AsyncSession,
    username: str,
    is_admin: bool,
    type_user: Literal["manager", "technical specialist"],
) -> User:
    user = User(username=username, is_admin=is_admin, type_user=type_user)
    session.add(user)
    await session.commit()
    print("user", user)
    return user


async def generate_data_for_users(session):
    await create_user(
        session=session, username="Vova", is_admin=True, type_user="manager"
    )
    await create_user(
        session=session,
        username="Vany",
        is_admin=False,
        type_user="technical specialist",
    )
    await create_user(
        session=session,
        username="Vity",
        is_admin=False,
        type_user="technical specialist",
    )
    await create_user(
        session=session, username="Anna", is_admin=False, type_user="manager"
    )
    await create_user(
        session=session,
        username="Kate",
        is_admin=True,
        type_user="technical specialist",
    )


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    user: User | None = await session.scalar(stmt)
    print(f"found user", username, user)
    return user


async def main():
    async with db_helper.session_factory() as session:
        # await generate_data_for_users(session)
        user_vova = await get_user_by_username(session=session, username="Vova")
        user_tonny = await get_user_by_username(session=session, username="Tonny")
        user_vity = await get_user_by_username(session=session, username="Vity")


if __name__ == "__main__":
    asyncio.run(main())
