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
