from typing import Any
from urllib.parse import urljoin

import requests as r
from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


class TokenBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(TokenBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> dict:
        credentials: HTTPAuthorizationCredentials = await super(
            TokenBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=403, detail="Invalid authentication scheme."
                )
            if not self.verify_token(credentials.credentials)[0]:
                raise HTTPException(
                    status_code=403, detail="Invalid token or expired token."
                )
            return self.verify_token(credentials.credentials)[1]
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_token(
        self, token: str
    ) -> tuple[bool, Any] | tuple[bool, dict[str, str]]:

        """
        Authenticate a user.
        """

        gitlab_url = urljoin("https://gitlab.com", f"/api/v4/user?access_token={token}")
        gitlab_res = r.get(gitlab_url)
        if gitlab_res.status_code == 200:
            response = {"token": token, "login": gitlab_res.json()["username"]}
            return True, response

        github_url, github_headers = "https://api.github.com/user", {
            "Authorization": f"token {token}"
        }
        github_res = r.get(github_url, headers=github_headers)
        if github_res.status_code == 200:
            response = {"token": token, "login": github_res.json()["login"]}
            return True, response

        # If the user is not valid, return an error message.
        return False, {"error": "Invalid token."}
