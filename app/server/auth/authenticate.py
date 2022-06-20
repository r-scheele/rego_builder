import json

import requests as r
from fastapi import APIRouter
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
def get_token(code: str, client_id: str, client_secret: str) -> dict:
    res = r.post(
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
