from rego_build_api.server.models import RequestObject
from .build_rego_file import build_rego
from rego_build_api.server.github import initialize_repo, git_push

initiate_rule = "package httpapi.authz\nimport input\ndefault allow = false\n\n\n\n"
repo_url = "/Users/Abdulrahman/code/test-policy-repo"
email = "abdulrahmanolamilkena88@gmail.com"
name = "r-scheele"


def write_to_file(rule: RequestObject) -> dict:
    """
    Write the rego file to the local git repository
    :param key: rules
    :return: response dict to show the status of the request
    """
    # if user does not exist, create a new user
    # configure git credentials
    # check if there is an existing repo  - path to the repo, and clone it
    # if not, create a new repo
    repo = initialize_repo(repo_url, email, name)

    # with open(f"{repo_folder_path}auth.rego", "w") as file:
    #     result = initiate_rule + build_rego(rule.rules)

    #     file.write(result)

    # git_push(repo_path)
    return {"status": "success"}
