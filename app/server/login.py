import json

import requests as r
from fastapi import APIRouter
from starlette.responses import RedirectResponse
from jose import jwt
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
    result = json.loads(res.text)["access_token"]
    return {"acess_token": result}
