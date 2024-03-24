from pydantic import BaseModel, ConfigDict


class ProjectBase(BaseModel):
    name: str
    description: str
    user_id: int


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdatePartial(ProjectCreate):
    name: str | None = None
    description: str | None = None


class Project(ProjectBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
