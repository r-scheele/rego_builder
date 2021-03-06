import os

from app.server.github import GitHubOperations
from .build_rego_file import build_rego

initiate_rule = "package httpapi.authz\nimport input\ndefault allow = false\n\n\n\n"


class WriteRego:
    def __init__(self, access_token: str, github_repo_url: str, username: str) -> None:
        self.username = username
        self.access_token = access_token
        self.github_repo_url = github_repo_url
        self.github = GitHubOperations(
            self.github_repo_url, self.access_token, self.username
        )

    def write_to_file(self, policies: list) -> None:
        """
        Write the rego file to the local git repository
        :param policies: list of policies
        :return: response dict to show the status of the request
        """
        # Define file path
        file_path = f"{self.github.local_repo_path}/auth.rego"

        # Initialize repository
        self.github.initialize()

        result = "" if not policies else initiate_rule
        for policy in policies:
            result += build_rego(policy["rules"])

        with open(file_path, "w+") as file:
            file.write(result)
        # Update GitHub
        self.github.push()

    def delete_policy(self, policies: list) -> bool:
        file_path = f"{self.github.local_repo_path}/auth.rego"

        if not os.path.exists(file_path):
            raise FileNotFoundError

        # check if there is no policy belonging to the user, in that repository, if so, initiate_rule = ""

        self.write_to_file(policies)
        return True
