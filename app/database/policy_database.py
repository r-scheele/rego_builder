from fastapi import HTTPException
from tinydb import Query, TinyDB

from app.config.config import settings
from app.schemas.rules import RequestObject, UpdateRequestObject


class PolicyDatabase:
    def __init__(self, database_url: str):
        self.database = TinyDB(database_url)
        self.store = Query()

    def get_policy(self, policy_name: str, owner: str) -> dict:
        return self.database.get(
            self.store.name == policy_name and self.store.owner == owner
        )

    def add_policy(self, policy: dict, owner: str) -> dict:
        if self.exists(policy["name"], owner):
            raise HTTPException(
                status_code=409, detail="Rules with the same name already exist"
            )
        self.database.insert(policy)
        return policy

    def update_policy(self, policy_name: str, policy: dict, owner: dict) -> None:
        self.database.update(
            policy, self.store.name == policy_name and self.store.owner == owner
        )

    def exists(self, policy_name: str, owner: str) -> bool:
        doc = self.database.get(
            self.store.name == policy_name and self.store.owner == owner
        )
        return doc["name"] == policy_name

    def delete_policy(self, policy_name: str, owner: str) -> None:
        self.database.remove(
            self.store.name == policy_name and self.store.owner == owner
        )

    def get_policies(self, owner: str) -> list:
        return self.database.search(self.store.owner == owner)


def get_db() -> PolicyDatabase:
    return PolicyDatabase(settings.DATABASE_PATH)
