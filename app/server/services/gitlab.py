from functools import lru_cache

import gitlab.exceptions
from gitlab import Gitlab


@lru_cache(maxsize=1)
class GitLabOperations:
    """Performs all operations needed to push the changes to the remote repository on the gitlab server"""

    def __init__(self, repo_id: int, access_token: str) -> None:
        """Initializes the class with base arguments

        :param repo_id: the id of the remote repository.
        :param access_token: the gitlab access token to authorize access to the remote repository.
        """

        self.access_token = access_token
        self.repo_id = repo_id

        self.gitlab = Gitlab(url="https://gitlab.com", oauth_token=self.access_token)

        # Initialize Gitlab instance
        self.gitlab.auth()

        # Retrieve the repository
        self.repo = self.gitlab.projects.get(self.repo_id)

    def prepare_data_and_commit(self, policy: str, action: str) -> bool:
        """
        prepare policy for commit and commit it

        :param policy: - policy string to be written to the file
        :param action: - action to be performed on the policy

        :returns: True if a commit was successful, False otherwise
        """
        data = {
            # Once this works, enable user set the branch or use default branch instead.
            'branch': 'main',
            'commit_message': 'Policy update from the OPA Manager',
            'actions': [
                {
                    'action': action,
                    'file_path': 'auth.rego',
                    'content': policy,
                },
            ]
        }

        try:
            # Commit the changes
            self.repo.commits.create(data)

        except gitlab.exceptions.GitlabCreateError:
            data['actions'][0]['action'] = 'create'

            # Commit the changes
            self.repo.commits.create(data)
            return True

        except gitlab.exceptions.GitlabError:
            return False

    def delete_policy(self) -> bool:
        data = {
            "branch": "master",
            "commit_message": "Policy deleted by the OPA Manager",
            "actions": [
                {
                    "action": "delete",
                    "file_path": "auth.rego",
                }
            ],
        }

        try:
            self.repo.commits.create(data)
        except gitlab.exceptions.GitlabCreateError:
            return False
        return True

    def repo_url_from_id(self) -> str:
        return self.repo.web_url
