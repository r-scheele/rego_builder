from fastapi import HTTPException
from tinydb import Query, TinyDB

from app.config.config import settings


class PolicyDatabase:
    """
    Performs all CRUD operations on the policy
    """

    def __init__(self, database_url: str):
        """
        Initializes the database class with base arguments

        :param database_url: the url of the policy database (tinydb)
        """
        self.database = TinyDB(database_url)
        self.store = Query()

    def get_policy(self, policy_name: str, owner: str) -> dict:
        """Returns the policy with the given name and owner

        :param policy_name: the name to identify the policy
        :param owner: the user that writes the policy
        :returns: the policy with the given name and owner
        """
        policy = self.database.get(
            (self.store.name == policy_name) & (self.store.owner == owner)
        )
        if policy:
            return policy
        return {}

    def add_policy(self, policy: dict, owner: str) -> dict:
        """Adds a policy to the database if it doesn't exist

        :param policy: the policy to add to the database
        :param owner: the user that writes the policy
        :return: the policy that was added to the database
        """
        if self.exists(policy["name"], owner):
            raise HTTPException(
                status_code=409, detail="Rules with the same name already exist"
            )
        self.database.insert(policy)
        return policy

    def update_policy(self, policy_name: str, policy: dict, owner: str) -> None:
        """Identify the policy with the given name and owner and update it

        :param policy_name: the name to identify the policy
        :param policy: the new policy to update the old one with
        :param owner: the user that writes the policy

        :return: None
        """
        policy = self.get_policy(policy_name, owner)

        self.database.update(
            policy, (self.store.name == policy_name) & (self.store.owner == owner)
        )

    def exists(self, policy_name: str, owner: str) -> bool:
        """Checks if a policy with the given name and owner exists

        :param policy_name: the name to identify the policy
        :param owner: the user that writes the policy

        :return: True if the policy exists, False otherwise
        """
        doc = self.database.get(
            (self.store.name == policy_name) & (self.store.owner == owner)
        )
        is_exist = True if doc else False
        return is_exist

    def delete_policy(self, policy_name: str, owner: str, repo_url: str) -> None:
        """Identify the policy with the given name and owner and delete it

        :param policy_name: the name to identify the policy
        :param owner: the user that writes the policy"""
        self.database.remove(
            (self.store.name == policy_name)
            & (self.store.owner == owner)
            & (self.store.repo_url == repo_url)
        )

    def get_policies(self, owner: str) -> list:
        """Returns all the policies of the given owner

        :param owner: the user that writes the policy
        :return: all the policies of the given owner
        """
        return self.database.search((self.store.owner == owner))
        policies = self.database.search(self.store.owner == owner)
        return policies


def get_db() -> PolicyDatabase:
    return PolicyDatabase(settings.DATABASE_PATH)
