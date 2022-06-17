from typing import Any

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

        url = "https://api.github.com/user"
        headers = {"Authorization": f"token {token}"}
        res = r.get(url, headers=headers)
        # If the user is valid, return the user's information.
        if res.status_code == 200:
            response = {"token": token, "login": res.json()["login"]}
            return True, response
        # If the user is not valid, return an error message.
        return False, {"error": "Invalid token."}
