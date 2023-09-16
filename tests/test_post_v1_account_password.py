from services.dm_api_account import DmApiAccount
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_password():
    api = DmApiAccount(host='http://localhost:5051')
    json = {
        "login": "login_7",
        "email": "login_7@mail.ru"
    }
    response = api.account.post_v1_account_password(
        json=json
    )
    print(response)
