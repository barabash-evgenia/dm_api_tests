from services.dm_api_account import Facade
import structlog
from dm_api_account.models.reset_password_model import ResetPassword
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_password():
    api = Facade(host='http://localhost:5051')
    json = ResetPassword(
        login="login_21",
        email="login_21@mail.ru"
    )
    response = api.account_api.post_v1_account_password(json=json, status_code=201)
    assert_that(response.resource, has_properties(
        {
            "login": "login_21",
            "roles": [UserRole.guest, UserRole.player],
        }
    ))
