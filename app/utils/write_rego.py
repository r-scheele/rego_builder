import os

from app.config.config import settings
from app.server.github import GitHubOperations

from .build_rego_file import build_rego

github = GitHubOperations(settings.GITHUB_URL)

initiate_rule = "package httpapi.authz\nimport input\ndefault allow = false\n\n\n\n"


def write_to_file(rule, operation: str = "write") -> dict:
    """
    Write the rego file to the local git repository
    :param rule: rules
    :return: response dict to show the status of the request
    """
    # Define file path
    file_path = f"{github.local_repo_path}/auth.rego"

    # Initialize repository
    github.initialize()

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
    github.push()


def delete_policy_file() -> bool:
    file_path = f"{github.local_repo_path}/auth.rego"

    if not os.path.isfile(file_path):
        raise FileNotFoundError

    file = open(file_path, "w")
    file.close()

    # Update GitHub
    github.push()
    return True
