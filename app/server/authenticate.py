import json

import requests as r
from fastapi import APIRouter
from jose import jwt
from starlette.responses import RedirectResponse

from app.config.config import settings

router = APIRouter()


@router.get("/login")
def authorize():
    res = r.get(
        url="https://github.com/login/oauth/authorize",
        data={
            "client_id": settings.CLIENT_ID,
            "redirect_uri": "http://localhost:8080/token",
        },
    )
    return RedirectResponse(url=res.url)


@router.get("/token")
def get_token(code: str):
    res = r.post(
        url="https://github.com/login/oauth/access_token",
        headers={"Accept": "application/json"},
        data={
            "client_id": settings.CLIENT_ID,
            "client_secret": settings.CLIENT_SECRET,
            "code": code,
        },
    )
    res = json.loads(res.text)
    access_token, expires_in = res["access_token"], res["expires_in"]

    return {"acess_token": access_token, "expires_in": expires_in}


def verify_token(acess_token: str):

    """
    Authenticate a user.
    """

    # Send request to the GitHub API to check if the user is valid.
    url = "https://api.github.com/user"
    headers = {"Authorization": f"token {acess_token}"}
    res = r.get(url, headers=headers)
    # If the user is valid, return the user's information.
    if res.status_code == 200:
        return res.json()
    # If the user is not valid, return an error message.
    return {"error": "Invalid token."}
