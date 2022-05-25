import os

from app.config.config import settings
from app.schemas.rules import RequestObject
from app.server.github import GitHubOperations

from .build_rego_file import build_rego

github = GitHubOperations(settings.GITHUB_URL)

initiate_rule = "package httpapi.authz\nimport input\ndefault allow = false\n\n\n\n"


def write_to_file(rule: RequestObject) -> dict:
    """
    Write the rego file to the local git repository
    :param rule: rules
    :return: response dict to show the status of the request
    """
    # Define file path
    file_path = f"{github.local_repo_path}/auth.rego"

    # Initialize repository
    github.initialize()

    # Create rego file.
    with open(file_path, "w") as file:
        result = initiate_rule + build_rego(rule.rules)

        file.write(result)

    # Push to GitHub
    github.push()

    return {"status": "success"}


def delete_policy_file() -> bool:
    file_path = f"{github.local_repo_path}/auth.rego"

    if not os.path.isfile(file_path):
        raise FileNotFoundError

    file = open(file_path, "w")
    file.close()

    # Update GitHub
    github.push()
    return True
