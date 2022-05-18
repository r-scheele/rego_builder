from git import Repo, Git


## You should have a local git repository and initialize the path
repo_url = "/Users/Abdulrahman/code/opal-policy-example/"


PATH_OF_GIT_REPO = f"{repo_url}.git"  # make sure .git folder is properly configured
COMMIT_MESSAGE = "comment from python script"


def git_push():
    """
    Push the changes to the remote repository
    """
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name="origin")
        origin.push()
    except:
        print("Some error occured while pushing the file to github")
