from services.dm_api_account import DmApiAccount


def test_put_v1_account_email():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "login_5",
        "email": "login_55555@mail.ru",
        "password": "login_5"
    }
    response = api.account.put_v1_account_email(
        json=json
    )
    print(response)