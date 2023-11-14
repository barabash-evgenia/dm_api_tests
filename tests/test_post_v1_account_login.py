from services.dm_api_account import DmApiAccount
import structlog
from dm_api_account.models.login_credentials_model import LoginCredentialsModel

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    api = DmApiAccount(host='http://localhost:5051')
    json = LoginCredentialsModel(
        login="login_23",
        password="login_23",
        remember_me=True
    )
    response = api.login.post_v1_account_login(
        json=json
    )
    assert response.status_code == 200, f'Статус код ответа должен быть равен 200, но он равен {response.status_code}'
