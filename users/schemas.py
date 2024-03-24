from typing import Literal

from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    username: str
    password: str
    is_admin: bool = False
    type_user: Literal["manager", "technical specialist"]


class UserCreate(UserBase):
    pass


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
