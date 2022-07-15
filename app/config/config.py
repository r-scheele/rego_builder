from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_PATH: Optional[str] = ""
    DATABASE_PATH: Optional[str] = ""
    TEST_DATABASE_PATH: Optional[str] = ""
    OPAL_SERVER_DATA_URL: Optional[str] = ""
    ENVIRONMENT: Optional[str] = "production"
    GITLAB_CLIENT_ID: Optional[str] = ""
    GITLAB_CLIENT_SECRET: Optional[str] = ""

    # POSTGRES CONNECTION
    HOST: Optional[str] = ""
    PASSWORD: Optional[str] = ""
    DATABASE: Optional[str] = ""
    DB_USER: Optional[str] = ""

    class Config:
        env_file = ".env"


settings = Settings()
