from services.dm_api_account import DmApiAccount


def test_put_v1_account_token():
    api = DmApiAccount(host='http://localhost:5051')
    response = api.account.put_v1_account_token(
        '0c49543a-a80e-4a39-8019-6b3d8f5a34f1'
    )
    print(response)
