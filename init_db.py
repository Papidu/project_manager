import asyncio
from typing import Literal

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, User


async def create_user(
        session: AsyncSession,
        username: str,
        password: str,
        is_admin: bool,
        type_user: Literal["manager", "technical specialist"]) -> User:
    user = User(username=username, password=password, is_admin=is_admin, type_user=type_user)
    session.add(user)
    await session.commit()
    print("user", user)
    return user


async def get_user_by_username(session: AsyncSession, username: str) -> User | None:
    stmt = select(User).where(User.username == username)
    user: User | None = await session.scalar(stmt)
    print("found user", username, user)
    return user


async def main():
    async with db_helper.session_factory() as session:
        # await create_user(session=session, username="maksim", password="1234", is_admin=True, type_user="manager")
        # await create_user(session=session, username="mary", password="123", is_admin=False, type_user="manager")
        # await create_user(session=session, username="samuel", password="12", is_admin=True, type_user="technical specialist")
        # await create_user(session=session, username="jonatan", password="1", is_admin=False, type_user="technical specialist")
        # await create_user(session=session, username="sam", password="1", is_admin=True, type_user="technical specialist")
        # await create_user(session=session, username="john", password="1", is_admin=False, type_user="technical specialist")
        user_sam = await get_user_by_username(session=session, username="sam")
        user_john = await get_user_by_username(session=session, username="john")


if __name__ == "__main__":
    asyncio.run(main())