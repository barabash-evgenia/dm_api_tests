from services.dm_api_account import DmApiAccount
import structlog
from dm_api_account.models.change_password_model import ChangePasswordModel
structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    api = DmApiAccount(host='http://localhost:5051')
    json = ChangePasswordModel(
        login="login_21",
        token="e5630c2a-2aa9-40db-b741-321e137b1e3b",
        old_password="login_21",
        new_password="login_211"
    )
    response = api.account.put_v1_account_password(
        json=json
    )
    assert response.status_code == 200, f'Статус код ответа должен быть равен 200, но он равен {response.status_code}'

