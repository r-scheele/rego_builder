import os

from app.config.config import settings

default_path = settings.BASE_PATH


def init_dir() -> None:
    if not os.path.exists(default_path):
        os.mkdir(default_path)
    if not os.path.exists(settings.DATABASE_PATH):
        with open(settings.DATABASE_PATH, "w") as f:
            f.write("{}")


if __name__ == "__main__":
    init_dir()