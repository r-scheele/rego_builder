import os

import requests as r
from git import Repo, exc

## You should have a local git repository and initialize the path
from rego_build_api.config.config import settings

access_token = settings.GITHUB_ACCESS_TOKEN

COMMIT_MESSAGE = "updates from from application"

default_path = "/Users/youngestdev/Work" # At some point, we'll instruct our app to create a fastgeoapi in a location such as /usr/src etc.


def initialize_repo(repo_url: str, email: str, name: str):
    repo_name_from_url = repo_url.split("/")[-1]
    local_repo = f"{default_path}/{repo_name_from_url}"
    # Skip if the folder exists

    if os.path.exists(local_repo):
        return {
            "status": "success",
            "repo_path": f"{default_path}/{repo_name_from_url}"
        }

    os.mkdir(local_repo)

    try:
        repo = Repo(repo_url)
        repo_path = repo.git_dir
    except exc.NoSuchPathError:
        try:
            repo = Repo.init(local_repo)
            with repo.config_writer() as git_config:
                git_config.set_value("user", "email", email).release()
                git_config.set_value("user", "name", name).release()
            repo_path = repo.git_dir
        except exc.GitCommandError:
            return {"status": "error"}
    repo_name = repo_path.strip(".git").split("/")[-1]

    # Check if the url is valid - The one in the request
    try:
        remote_url = f"https://api.github.com/repos/{name}/{repo_name}"
        res = r.get(remote_url)
        if res.status_code == 200:
            return {"status": "success", "url": repo_path}
        else:
            # create a remote repository /repos/{owner}/{repo}'
            remote_repository = r.post(
                f"https://api.github.com/repos/{name}/repo",
                headers={
                    "Authorization": f"token {access_token}",
                },
                data={
                    "name": repo_name,
                    "private": False,
                },
            )
            return {
                "status": "success",
                "repo_path": f"{default_path}/{repo_name}"
            }
    except exc.GitCommandError:
        return {"status": "error"}


def git_push(path: str):
    """
    Push the changes to the remote repository
    """

    # Set target URL.
    repo_name = path.split("/")[-1]
    target_url = f"https://github.com/{settings.GITHUB_USERNAME}/{repo_name}"
    try:
        repo = Repo(f"{path}/.git")
        repo.git.add(update=True)
        repo.index.add([f"{path}/auth.rego"])
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
