from app.server.services.github_operations import GitHubOperations

from ..server.services.gitlab_operations import GitLabOperations
from .build_rego_file import build_rego

initiate_rule = "package httpapi.authz\nimport input\ndefault allow = false\n\n\n\n"


class WriteRego:
    """Writes policy definition"""

    def __init__(
        self,
        access_token: str,
        repo_url: str,
        username: str,
        provider: str = "github",
        repo_id: int = None,
    ) -> None:
        """
        Initializes the class

        params: access token, repo url, username, repo provider, repo id
        return: None
        """

        self.username = username
        self.access_token = access_token
        self.repo_url = repo_url
        self.repo_id = repo_id
        self.provider = provider

        if self.provider == "github":
            self.github = GitHubOperations(
                self.repo_url, self.access_token, self.username
            )

        if self.provider == "gitlab":
            self.gitlab = GitLabOperations(self.repo_id, self.access_token)

    def write_to_file(self, policies: list) -> None:
        """
        Write the rego file to the local git repository

        param list: list of policies
        return: None
        """

        result = "" if not policies else initiate_rule
        for policy in policies:
            if not policy:
                continue
            result += build_rego(policy["rules"])

        if not policies:
            result = ""

        if self.provider == "gitlab":
            self.gitlab.prepare_data_and_commit(result, "update")
            return

        if self.provider == "github":
            # Define file path
            file_path = f"{self.github.local_repo_path}/auth.rego"

            # Initialize repository
            self.github.initialize_github()

            with open(file_path, "w+") as file:
                file.write(result)
            # Update GitHub
            self.github.github_push()

        return
