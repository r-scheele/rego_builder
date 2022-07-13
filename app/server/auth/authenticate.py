import json

from fastapi import APIRouter
import requests as rest_client
from fastapi import APIRouter
from starlette.responses import RedirectResponse
from starlette.requests import Request

router = APIRouter()


from app.config.config import settings


# @router.get("/github/login")
# async def login_github():
#     APP_ID, REDIRECT_URI = (settings.GITHUB_CLIENT_ID, "http://localhost:8080/token")
#     url = f"https://github.com/login/oauth/authorize?client_id={APP_ID}&redirect_uri={REDIRECT_URI}&response_type=code"
#     return RedirectResponse(url=url)


# @router.get("/gitlab/login")
# async def login_gitlab():
#     APP_ID, REDIRECT_URI = (
#         settings.GITLAB_CLIENT_ID,
#         "http://localhost:8080/api/auth/callback/gitlab",
#     )
#     url = f"https://gitlab.com/oauth/authorize?client_id={APP_ID}&redirect_uri={REDIRECT_URI}&response_type=code"
#     return RedirectResponse(url=url)


@router.get("/api/auth/callback/gitlab")
async def get_token_from_gitlab(
    code: str, client_id: str, client_secret: str, redirect_uri: str
):
    res = rest_client.post(
        f"https://gitlab.com/oauth/token",
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": redirect_uri,
            # "redirect_uri": "http://localhost:8080/api/auth/callback/gitlab",
        },
    )
    json_res = res.json()
    access_token, expires_in = json_res["access_token"], json_res["expires_in"]
    return {"access_token": access_token, "expires_in": expires_in}


@router.get("/token")
def get_token_from_github(code: str, client_id: str, client_secret: str) -> dict:
    res = rest_client.post(
        url="https://github.com/login/oauth/access_token",
        headers={"Accept": "application/json"},
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
        },
    )
    res = json.loads(res.text)
    access_token, expires_in = res["access_token"], res["expires_in"]
    return {"access_token": access_token, "expires_in": expires_in}
