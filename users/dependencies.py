import secrets
from typing import Annotated

from fastapi import Depends, Path, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from users import crud
from core.models import db_helper, User


security = HTTPBasic()


async def user_by_id(
    user_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> User:
    user = await crud.get_user(session=session, user_id=user_id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User {user_id} not found!",
    )


async def get_auth_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> User:
    unauthorized_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )
    user = await crud.get_user_by_username(
        session=session, username=credentials.username
    )
    if user is None:
        raise unauthorized_exc
    if not secrets.compare_digest(
        credentials.password.encode("utf-8"),
        user.password.encode("utf-8"),
    ):
        raise unauthorized_exc
    print(user, type(user))
    return user