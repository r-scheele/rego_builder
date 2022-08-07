import gitlab
import requests as r
from fastapi import APIRouter, Depends

from app.server.auth.authorize import TokenBearer
from dataclasses import dataclass

router = APIRouter(tags=["Repo Management"], prefix="/user/repos")


@dataclass
class RepoStructure:
    name: str
    id: int
    url: str
    owner: str


@router.get("/github")
async def get_public_and_private_repo(
        dependencies=Depends(TokenBearer()),
) -> list:
    url = f"https://api.github.com/search/repositories?q=user:{dependencies['login']}"
    repos = r.get(
        url=url,
        headers={"Authorization": f"token {dependencies['token']}"},
    ).json()

    repos = [
        {
            "name": repo["name"],
            "html_url": repo["html_url"],
            "owner": repo["owner"]["login"],
        }
        for repo in repos["items"]
    ]
    return repos


@router.get("/gitlab")
async def get_public_and_private_repo_gitlab(
        dependencies=Depends(TokenBearer()),
) -> list:
    gl = gitlab.Gitlab("https://gitlab.com", oauth_token=dependencies["token"])
    gl.auth()

    unfiltered_repos = gl.projects.list(owned=True)
    repos = []

    for repo in unfiltered_repos:
        r = repo.asdict()
        repos.append(RepoStructure(
            name=r["name"],
            id=r["id"],
            url=r["web_url"],
            owner=r["namespace"]["full_path"],
        ))

    return repos
