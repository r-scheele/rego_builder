import os

import requests as r
from git import Repo

from config.config import settings

access_token = settings.GITHUB_ACCESS_TOKEN

COMMIT_MESSAGE = "updates from from application"

default_path = "/tmp/fastgeoapi"


def initialize_repo(repo_url: str) -> dict:
    # Create the default path
    if not os.path.exists(default_path):
        os.mkdir(default_path)

    repo_name = repo_url.strip(".git").split("/")[-1]
    local_repo_path = f"{default_path}/{repo_name}"

    # Check if the repo already exists
    if os.path.exists(local_repo_path):
        return {
            "status": "success",
            "repo_path": default_path,
            "repo_git_path": f"{local_repo_path}/.git"

        }

    os.mkdir(local_repo_path)

    # Check if the URL is valid

    remote_url = f"https://api.github.com/repos/{settings.GITHUB_USERNAME}/{repo_name}"
    res = r.get(remote_url)
    if res.status_code != 200:
        return {
            "status_code": res.status_code,
            "message": res.json()
        }

    # Clone the repo to the server
    initialized_repo = Repo.clone_from(repo_url, local_repo_path)
    repo_git_path = initialized_repo.git_dir

    return {
        "repo_path": local_repo_path,
        "repo_git_path": repo_git_path
    }


def git_push(repo_path: str, git_path: str) -> None:
    """
    Push the changes to the remote repository
    """

    # Set target URL.
    target_url = settings.GITHUB_URL
    try:
        repo = Repo(git_path)
        repo.git.add(update=True)
        repo.index.add([f"{repo_path}/auth.rego"])
        repo.index.commit(COMMIT_MESSAGE)
        remotes = repo.remotes
        if not remotes:
            repo.create_remote("origin", target_url)
        if remotes[0].name != "origin":
            repo.create_remote("origin", target_url)
        origin = repo.remote(name="origin")
        origin.pull()
        origin.push()
    except Exception:
        raise Exception
