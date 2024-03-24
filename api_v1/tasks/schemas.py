from typing import Literal
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column, String, Integer, DateTime, text, ForeignKey
from datetime import datetime


class TaskBase(BaseModel):
    name: str
    status: Literal["new", "progress", "done"]
    user_id: int
    project_id: int


class TaskCreate(TaskBase):
    pass


class TaskUpdatePartial(TaskCreate):
    status: Literal["new", "progress", "done"] | None = None


class Task(TaskBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
