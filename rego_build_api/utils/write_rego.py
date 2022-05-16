from rego_build_api.server.models import RequestObject
from .build_rego_file import build_rego
from rego_build_api.server.github import repo_url, git_push

initiate_rule = "package httpapi.authz\nimport input\ndefault allow = false\n\n\n\n"


def write_to_file(rule: RequestObject) -> dict:
    """
    Write the rego file to the local git repository
    :param key: rules
    :return: response dict to show the status of the request
    """

    with open(f"{repo_url}auth.rego", "w") as file:
        result = initiate_rule + build_rego(rule.rules)

        file.write(result)
    git_push()
    return {"status": "success"}
