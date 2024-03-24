from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Literal, TYPE_CHECKING
from sqlalchemy import String, DateTime, text, ForeignKey
from datetime import datetime
from .base import Base


if TYPE_CHECKING:
    from .user import User
    from .project import Project


class Task(Base):
    name: Mapped[str]
    status: Mapped[Literal["new", "progress", "done"]]
    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        server_default=text("current_timestamp"),
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        server_default=text("current_timestamp"),
        onupdate=text("current_timestamp"),
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id"),
    )

    user: Mapped["User"] = relationship(back_populates="tasks")
    project: Mapped["Project"] = relationship(back_populates="tasks")
