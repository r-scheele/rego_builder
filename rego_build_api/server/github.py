import os
from git import Repo, exc
import requests as r

## You should have a local git repository and initialize the path
from rego_build_api.config.config import settings

access_token = settings.GITHUB_ACCESS_TOKEN

COMMIT_MESSAGE = "updates from from application"


def git_push(path: str):
    """
    Push the changes to the remote repository
    """
    try:

        repo = Repo(path)
        print("here second")
        repo.git.add(update=True)
        repo.index.add([f"{settings.GITHUB_PATH}auth.rego"])
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name="origin")

        origin.pull()
        origin.push()
    except Exception:
        raise Exception


def initialize_repo(repo_url: str, email: str, name: str):

    try:
        repo = Repo(repo_url)
        repo_path = repo.git_dir
    except exc.NoSuchPathError:
        os.mkdir(repo_url)
        try:
            repo = Repo.init(repo_url)
            with repo.config_writer() as git_config:
                git_config.set_value("user", "email", email).release()
                git_config.set_value("user", "name", name).release()
            repo_path = repo.git_dir
        except exc.GitCommandError:
            return {"status": "error"}

    repo_name = "experiments"

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
            return {"status": "success", "url": repo_path}
    except exc.GitCommandError:
        return {"status": "error"}
