from fastapi import APIRouter, Depends
import requests as r

from app.server.auth.authorize import TokenBearer

router = APIRouter()


@router.get("/user/repos")
async def get_public_and_private_repo(
    dependencies=Depends(TokenBearer()),
) -> list:

    url = f"https://api.github.com/search/repositories?q=user:{dependencies['login']}"
    repos = r.get(
        url=url,
        headers={"Authorization": f"token {dependencies['token']}"},
    ).json()

    return [
        {
            "name": repo["name"],
            "html_url": repo["html_url"],
            "owner": repo["owner"]["login"],
        }
        for repo in repos["items"]
    ]


@router.get("/user/repos/gitlab")
async def get_public_and_private_repo_gitlab(
    dependencies=Depends(TokenBearer()),
) -> list:

    url = f"https://gitlab.com/api/v4/users/{dependencies['login']}/projects"
    repos = r.get(
        url=url,
        headers={"Authorization": f"Bearer {dependencies['token']}"},
    ).json()

    return [
        {
            "name": repo["name"],
            "html_url": repo["web_url"],
            "owner": repo["owner"]["username"],
        }
        for repo in repos
    ]
