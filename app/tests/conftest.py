from app.config.config import settings
from app.database.policy_database import PolicyDatabase, get_db

import os
import pytest
from starlette.testclient import TestClient

from app.server.api import app


def override_get_db():
    return PolicyDatabase(settings.TEST_DATABASE_PATH)


@pytest.fixture(scope="module")
def client():
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app=app)  # testing happens here
    os.remove(settings.TEST_DATABASE_PATH)
