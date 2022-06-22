import os

from app.config.config import settings
from app.server.github import GitHubOperations
from .build_rego_file import build_rego

initiate_rule = "package httpapi.authz\nimport input\ndefault allow = false\n\n\n\n"


class WriteRego:
    def __init__(self, access_token: str) -> None:
        self.access_token = access_token
        self.github = GitHubOperations(settings.GITHUB_URL, self.access_token)

    def write_to_file(self, policies: list) -> None:
        """
        Write the rego file to the local git repository
        :param rule: rules
        :param operation: write or update
        :return: response dict to show the status of the request
        """
        # Define file path
        file_path = f"{self.github.local_repo_path}/auth.rego"

        # Initialize repository
        self.github.initialize()

        result = initiate_rule
        for policy in policies:
            result += build_rego(policy["rules"])

        with open(file_path, "w") as file:
            file.write(result)
        # Update GitHub
        self.github.push()

    def delete_policy(self, policies: list) -> bool:
        file_path = f"{self.github.local_repo_path}/auth.rego"

        if not os.path.exists(file_path):
            raise FileNotFoundError

        self.write_to_file(policies)
        return True
