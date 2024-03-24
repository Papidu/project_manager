from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from .base import Base

if TYPE_CHECKING:
    from .project import Project


class Subproject(Base):
    name: Mapped[str]
    description: Mapped[str]
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id"),
    )

    project: Mapped["Project"] = relationship(back_populates="projects")
