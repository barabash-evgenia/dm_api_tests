import requests


def put_v1_account_password():
    """
    Change registered user password
    :return:
    """
    url = "http://localhost:5051/v1/account/password"

    payload = {
        "login": "login_114",
        "token": "d39efcf3-8064-43cb-9df6-b878de4ab866",
        "oldPassword": "login_114",
        "newPassword": "login_444"
    }
    headers = {
        'X-Dm-Auth-Token': '',
        'X-Dm-Bb-Render-Mode': '',
        'Content-Type': 'application/json',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="PUT",
        url=url,
        headers=headers,
        json=payload
    )
    return response
