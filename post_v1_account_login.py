import requests


def post_v1_account_login():
    """
    Authenticate via credentials
    :return:
    """
    url = "http://localhost:5051/v1/account/login"

    payload = {
        "login": "login_114",
        "password": "login_114",
        "rememberMe": False
    }
    headers = {
        'X-Dm-Bb-Render-Mode': '',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="POST",
        url=url,
        headers=headers,
        json=payload
    )
    return response
