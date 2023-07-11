import requests


def put_v1_account_email():
    """
    Change registered user email
    :return:
    """
    url = "http://localhost:5051/v1/account/email"

    payload = {
        "login": "login_114",
        "password": "login_114",
        "email": "login_444@mail.ru"
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
