from app.config.config import settings
from app.schemas.rules import RequestObject
from fastapi import HTTPException
from tinydb import Query
from tinydb import TinyDB


class PolicyDatabase:
    def __init__(self, database_url: str):
        self.database = TinyDB(database_url)
        self.store = Query()

    def get_policy(self, policy_name: str) -> dict:
        return self.database.get(self.store.name == policy_name)

    def add_policy(self, policy: RequestObject) -> None:
        if self.get_policy(policy["name"]):
            raise HTTPException(
                status_code=409, detail="Rules with the same name already exist"
            )
        self.database.insert(policy)
        return policy

    def update_policy(self, policy_name: str, policy: dict) -> None:
        self.database.update(policy, self.store.name == policy_name)

    def exists(self, policy_name: str) -> bool:
        return self.database.contains(self.store.name == policy_name)

    def delete_policy(self, policy_name: str) -> None:
        self.database.remove(self.store.name == policy_name)


def get_db():
    return PolicyDatabase(settings.DATABASE_PATH)
