import os

from app.config.config import settings
from app.server.github import GitHubOperations
from .build_rego_file import build_rego

initiate_rule = "package httpapi.authz\nimport input\ndefault allow = false\n\n\n\n"


class WriteRego:
    def __init__(self, access_token: str) -> None:
        self.access_token = access_token
        self.github = GitHubOperations(settings.GITHUB_URL, access_token)

    def write_to_file(self, rule: dict, operation: str = "write") -> None:
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

        rule = {key: value for key, value in rule.items()}

        # check if the file exists
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                data = file.read()
                old_rule = data if operation == "write" and data else initiate_rule

        else:
            # write the file
            old_rule = initiate_rule
        result = old_rule + build_rego(rule["rules"])

        with open(file_path, "w") as file:
            file.write(result)
        # Update GitHub
        self.github.push()

    def delete_policy(self, policies) -> bool:
        file_path = f"{self.github.local_repo_path}/auth.rego"

        if not os.path.isfile(file_path):
            raise FileNotFoundError

        # build the new file
        print(policies)

        # # Update GitHub
        # self.github.push()
        return True
