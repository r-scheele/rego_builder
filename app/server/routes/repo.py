from dataclasses import dataclass

import gitlab
import requests as r
from fastapi import APIRouter, Depends

from app.server.auth.authorize_token import TokenBearer
from app.config.config import settings

router = APIRouter(tags=["Repo Management"], prefix="/user/repos")


@dataclass
class RepoStructure:
    """
    Represents the structure of a repository.
    """
    name: str
    id: int
    url: str
    owner: str


@router.get("/github")
async def get_public_and_private_repo(
    dependencies=Depends(TokenBearer()),
) -> list:
    """
    Get all public and private repositories from GitHub

    :param dependencies:
    """
    url = f"https://api.github.com/search/repositories?q=user:{dependencies['login']}"
    repos = r.get(
        url=url,
        headers={"Authorization": f"token {dependencies['token']}"},
    ).json()

    repos = [
        {
            "name": repo["name"],
            "id": repo["html_url"],
            "owner": repo["owner"]["login"],
        }
        for repo in repos["items"]
    ]
    return repos


@router.get("/gitlab")
async def get_public_and_private_repo_gitlab(
    dependencies=Depends(TokenBearer()),
) -> list:
    """
    Get all public and private repositories from a GitLab organization.

    :param dependencies: - token bearer object
    :returns: list of repositories
    """
    gl = gitlab.Gitlab("https://gitlab.com", oauth_token=dependencies["token"])
    gl.auth()

    repos = []

    glab_org_name = settings.ORG_NAME

    group = gl.groups.get(glab_org_name).asdict()

    for project in group["projects"]:
        repos.append(
            RepoStructure(
                name=project["name"],
                id=project["id"],
                url=project["web_url"],
                owner=project["namespace"]["name"],
            )
        )

    return repos
