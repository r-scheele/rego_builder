from jose import jwt
from app.config.config import settings
import requests as r


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
