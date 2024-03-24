from os import getenv
from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    db_url: str = "postgresql+asyncpg://postgres:1@localhost:5432/project_dev"
    db_echo: bool = True


setting = Setting()
