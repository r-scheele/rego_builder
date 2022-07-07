from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    BASE_PATH: Optional[str] = ""
    DATABASE_PATH: Optional[str] = ""
    TEST_DATABASE_PATH: Optional[str] = ""
    GITHUB_ACCESS_TOKEN: Optional[str] = ""
    GITHUB_USERNAME: Optional[str] = ""
    GITHUB_URL: Optional[str] = ""
    CLIENT_ID: Optional[str] = ""
    CLIENT_SECRET: Optional[str] = ""
    SECRET_KEY: Optional[str] = ""
    ALGORITHM: Optional[str] = ""
    OPAL_SERVER_DATA_URL: Optional[str] = ""
    ENVIRONMENT: Optional[str] = "production"

    # POSTGRES CONNECTION
    HOST: Optional[str] = ""
    PASSWORD: Optional[str] = ""
    DATABASE: Optional[str] = ""
    DB_USER: Optional[str] = ""

    class Config:
        env_file = ".env"


settings = Settings()
