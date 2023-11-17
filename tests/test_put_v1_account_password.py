from services.dm_api_account import Facade
import structlog
from dm_api_account.models.change_password_model import ChangePassword
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_password():
    api = Facade(host='http://localhost:5051')
    json = ChangePassword(
        login="login_21",
        token="e5630c2a-2aa9-40db-b741-321e137b1e3b",
        old_password="login_21",
        new_password="login_211"
    )
    response = api.account_api.put_v1_account_password(json=json, status_code=200)
    assert_that(response.resource, has_properties(
        {
            "login": "login_24",
            "roles": [UserRole.guest, UserRole.player],
        }
    ))
