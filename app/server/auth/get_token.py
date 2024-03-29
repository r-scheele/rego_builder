import json

import requests as rest_client
from fastapi import APIRouter

router = APIRouter(tags=["Token"])


@router.get("/gitlab/token")
async def get_token_from_gitlab(
    code: str, client_id: str, client_secret: str, redirect_uri: str
) -> dict:
    """Get the authorization token from GitLab."""

    res = rest_client.post(
        f"https://gitlab.com/oauth/token",
        data={
            "client_id": client_id,
            "client_secret": client_secret,
            "code": code,
            "grant_type": "authorization_code",
            "redirect_uri": redirect_uri,
        },
    )
    json_res = res.json()
    access_token, expires_in = json_res["access_token"], json_res["expires_in"]
    return {"access_token": access_token, "expires_in": expires_in}


@router.get("/github/token")
def get_token_from_github(code: str, client_id: str, client_secret: str) -> dict:
    """Get the authorization token from GitHub"""
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
