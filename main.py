import os

import uvicorn

from app.config.config import settings


default_path = settings.BASE_PATH


def init_dir() -> None:
    if not os.path.exists(default_path):
        os.mkdir(default_path)


if __name__ == "__main__":
    init_dir()
    if settings.ENVIRONMENT == "development":
        uvicorn.run("app.server.api:app", host="0.0.0.0", port=8080, reload=True)
    else:
        uvicorn.run("app.server.api:app", host="0.0.0.0", port=8080)
