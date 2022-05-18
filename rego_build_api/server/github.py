import os
from git import Repo, exc
import requests as r

## You should have a local git repository and initialize the path
access_token = "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"

COMMIT_MESSAGE = "comment from python script"


def git_push(path):
    """
    Push the changes to the remote repository
    """
    try:
        repo = Repo(path)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name="origin")
        origin.push()

        print("Pushed to remote repository")
    except:
        print("Some error occured while pushing the file to github")


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

    repo_name = repo_path.replace(".git", "").split("/")[-1]

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
            print(remote_repository.status_code)
            return {"status": "success", "url": repo_path}
    except exc.GitCommandError:
        print("Some error occured while initializing the remote repository")
        return {"status": "error"}
