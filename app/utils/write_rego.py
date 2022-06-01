import os
from app.config.config import settings
from app.schemas.rules import RequestObject
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
        # read the file
        with open(file_path, "r") as file:
            data = file.read() if operation == "write" else rule["old_state"]
    else:
        # create the file
        with open(file_path, "w") as file:
            data = initiate_rule

    result = data + build_rego(rule["rules"])

    if result:
        with open(file_path, "w") as file:
            file.write(result)
            # Update GitHub
            github.push()
            return {
                "status": "success",
                "message": "Policy successfully written to file",
                "old_state": data,
            }

    return {"status": "error", "message": "Policy is invalid"}


def delete_policy_file() -> bool:
    file_path = f"{github.local_repo_path}/auth.rego"

    if not os.path.isfile(file_path):
        raise FileNotFoundError

    file = open(file_path, "w")
    file.close()

    # Update GitHub
    github.push()
    return True
