import os
from functools import lru_cache

from git import Repo

from app.config.config import settings

COMMIT_MESSAGE = "Policy update from from application"

default_path = settings.BASE_PATH


@lru_cache(maxsize=1)
class GitHubOperations:
    """Performs all operations needed to push the changes to the remote repository on the github server"""

    def __init__(self, repo_url: str, access_token: str, username: str) -> None:
        """Initialize the class with the base arguments

        :param repo_url: the url of the remote repository.
        :param access_token: the github access token to authorize access to the remote repository.
        :param username: the username of the github user.

        :returns: None
        """

        self.username = username
        self.access_token = access_token
        self.repo_url = repo_url.lstrip("https://")
        self.complete_repo_url = (
            f"https://{self.username}:{self.access_token}@{self.repo_url}"
        )
        self.repo_name = repo_url.removesuffix(".git").split("/")[-1]
        self.local_repo_path = f"{default_path}/{self.repo_name}"
        self.repo_git_path = ""

    def initialize(self) -> None:
        """clones the remote repository if it doesn't exist, sets the local repository path for writing the changes.

        :param: None
        :returns: None
        """

        # Check if the repo already exists
        if os.path.exists(self.local_repo_path):
            self.repo_git_path = f"{self.local_repo_path}/.git"
            return

        os.mkdir(self.local_repo_path)

        # Clone the repo to the server
        initialized_repo = Repo.clone_from(self.complete_repo_url, self.local_repo_path)

        self.repo_git_path = initialized_repo.git_dir

    def push(self) -> None:
        """
        Initialize the rego file as a git repository, add the rego file,
        commit changes to the rego file, create a remote if it doesn't exist,
        pull commit history and push the changes to the remote repository.

        :param: None
        :returns: None
        """
        try:
            target_url = self.complete_repo_url
            repo = Repo(self.repo_git_path)
            repo.git.add(update=True)
            repo.index.add([f"{self.local_repo_path}/auth.rego"])
            repo.index.commit(COMMIT_MESSAGE)
            remotes = repo.remotes
            if not remotes:
                repo.create_remote("origin", target_url)
            if remotes[0].name != "origin":
                repo.create_remote("origin", target_url)
            origin = repo.remote(name="origin")
            origin.fetch()

            origin.push()
        except Exception:
            raise Exception
