from services.dm_api_account import DmApiAccount
import structlog
from dm_api_account.models.reset_password_model import ResetPasswordModel

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_password():
    api = DmApiAccount(host='http://localhost:5051')
    json = ResetPasswordModel(
        login="login_21",
        email="login_21@mail.ru"
    )
    response = api.account.post_v1_account_password(
        json=json
    )
    assert response.status_code == 200, f'Статус код ответа должен быть равен 200, но он равен {response.status_code}'
