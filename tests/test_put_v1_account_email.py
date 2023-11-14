from services.dm_api_account import DmApiAccount
import structlog
from dm_api_account.models.change_email_model import ChangeEmailModel

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    api = DmApiAccount(host='http://localhost:5051')
    json = ChangeEmailModel(
        login="login_24",
        email="login_24444@mail.ru",
        password="login_24"
    )
    response = api.account.put_v1_account_email(
        json=json
    )
    assert response.status_code == 200, f'Статус код ответа должен быть равен 200, но он равен {response.status_code}'

