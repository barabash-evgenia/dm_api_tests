from services.dm_api_account import DmApiAccount


def test_put_v1_account_password():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "login_7",
        "token": "0a0e662a-84b9-4201-9899-74ebdc54fea8",
        "oldPassword": "login_7",
        "newPassword": "login_77"
    }
    response = api.account.put_v1_account_password(
        json=json
    )
    print(response)
