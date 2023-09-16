from services.dm_api_account import DmApiAccount
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "login_7",
        "password": "login_77",
        "rememberMe": True
    }
    response = api.login.post_v1_account_login(
        json=json
    )
    print(response)
