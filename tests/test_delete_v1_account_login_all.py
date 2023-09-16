from services.dm_api_account import DmApiAccount


def test_delete_v1_account_login_all():
    api = DmApiAccount(host='http://localhost:5051', headers={
        'X-Dm-Auth-Token': 'IQJh+zgzF5DAdTdJZYMSq3R9bl4CKSMEV7m7ugTLKStOQZk8aUjJGgc67gkJbrqQbXaVqF9WOCt51pacJ3msFOnG0qlsiWHtakvKqf96yyrDVwiouhpLmTuVI7ioU6X2QfmkzA4Mg74= '})
    response = api.login.delete_v1_account_login_all(
    )
    print(response)



