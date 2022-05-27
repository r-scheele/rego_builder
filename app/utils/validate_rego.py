import requests as r


def validate_policy(policy: str) -> bool:
    """
    Validate the policy
    :param policy: policy
    :return: True if valid, False if invalid
    """

    # Define the url
    url = ""
    # Define the data
    data = {"query": policy}
    # Send the request
    response = r.post(url, json=data)
    # Check the status code
    return True if response.status_code == 200 else False
