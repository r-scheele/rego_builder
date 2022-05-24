from app.config.config import settings
from app.schemas.rules import RequestObject
from fastapi import HTTPException
from tinydb import Query
from tinydb import TinyDB

database = TinyDB(settings.DATABASE_PATH)
store = Query()


def get_policy(policy_name: str) -> dict:
    policy = database.get(store.name == policy_name)
    return policy


def add_policy(policy: RequestObject) -> None:
    if get_policy(policy.name):
        raise HTTPException(status_code=409, detail="Policy with supplied name exists.")
    database.insert(policy.dict())


def update_policy(policy_name: str, policy: dict) -> None:
    database.update(policy, store.name == policy_name)


def exists(policy_name: str) -> bool:
    return database.contains(store.name == policy_name)


def delete_policy(policy_name: str) -> None:
    database.remove(store.name == policy_name)
