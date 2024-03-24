from typing import Literal, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


if TYPE_CHECKING:
    from .task import Task
    from .project import Project


class User(Base):
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    is_admin: Mapped[bool]
    type_user: Mapped[Literal["manager", "technical specialist"]]

    tasks: Mapped[list["Task"] | None] = relationship(back_populates="user")
    projects: Mapped[list["Project"] | None] = relationship(back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r})"

    def __repr__(self):
        return str(self)
