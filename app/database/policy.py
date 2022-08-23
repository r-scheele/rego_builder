from fastapi import HTTPException
from tinydb import Query, TinyDB

from app.config.config import settings


class PolicyDatabase:
    def __init__(self, database_url: str):
        self.database = TinyDB(database_url)
        self.store = Query()

    def get_policy(self, policy_name: str, owner: str) -> dict:
        policy = self.database.get(
            (self.store.name == policy_name) & (self.store.owner == owner)
        )
        if policy:
            return policy
        return {}

    def add_policy(self, policy: dict, owner: str) -> dict:

        if self.exists(policy["name"], owner):
            raise HTTPException(
                status_code=409, detail="Rules with the same name already exist"
            )
        self.database.insert(policy)
        return policy

    def update_policy(self, policy_name: str, policy: dict, owner: str) -> None:
        policy = self.get_policy(policy_name, owner)

        self.database.update(
            policy, (self.store.name == policy_name) & (self.store.owner == owner)
        )

    def exists(self, policy_name: str, owner: str) -> bool:
        doc = self.database.get(
            (self.store.name == policy_name) & (self.store.owner == owner)
        )
        is_exist = True if doc else False
        return is_exist

    def delete_policy(self, policy_name: str, owner: str, repo_url: str) -> None:
        self.database.remove(
            (self.store.name == policy_name)
            & (self.store.owner == owner)
            & (self.store.repo_url == repo_url)
        )

    def get_policies(self, owner: str) -> list:
        policies = self.database.search(self.store.owner == owner)
        return policies


def get_db() -> PolicyDatabase:
    return PolicyDatabase(settings.DATABASE_PATH)
