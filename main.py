import os
import uvicorn
from app.config.config import settings

default_path = settings.BASE_PATH


def init_dir() -> None:
    if not os.path.exists(default_path):
        os.mkdir(default_path)


if __name__ == "__main__":
    init_dir()
    uvicorn.run("app.server.api:app", reload=True)
