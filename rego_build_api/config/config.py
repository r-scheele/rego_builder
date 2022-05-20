from pydantic import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    GITHUB_ACCESS_TOKEN: Optional[str] = ""
    GITHUB_PATH: Optional[str] = ""
    GITHUB_EMAIL: Optional[str] = ""
    GITHUB_USERNAME: Optional[str] = ""
    GITHUB_URL: Optional[str] = ""

    class Config:
        env_file = ".env"


settings = Settings()
