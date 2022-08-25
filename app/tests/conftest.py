import os

import pytest
from starlette.testclient import TestClient

from app.config.config import settings
from app.database.policy import PolicyDatabase, get_db
from app.server.api import app

default_path = settings.BASE_PATH


def init_dir() -> None:
    """Initializes the test directory"""

    if not os.path.exists(default_path):
        os.makedirs(default_path)
    if not os.path.exists(f"{default_path}/test.json"):
        with open(f"{default_path}/test.json", "w") as f:
            f.write("{}")


init_dir()


def override_get_db() -> PolicyDatabase:
    """Override the get_db function to return a fake database used for tests purpose"""

    return PolicyDatabase(f"{default_path}/test.json")


@pytest.fixture(scope="module")
def client() -> TestClient:
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app=app)
    os.remove(f"{default_path}/test.json")


@pytest.fixture(scope="module")
def authorized_client(client: TestClient) -> TestClient:

    """Authorize the client with an access token"""
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {settings.GITHUB_ACCESS_TOKEN}",
    }
    return client
