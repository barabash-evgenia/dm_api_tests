from services.dm_api_account import DmApiAccount
import structlog
from dm_api_account.models.login_credentials_model import LoginCredentials
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account_login():
    api = DmApiAccount(host='http://localhost:5051')
    json = LoginCredentials(
        login="login_23",
        password="login_23",
        remember_me=True
    )
    response = api.login.post_v1_account_login(json=json, status_code=200)
    assert_that(response.resource, has_properties(
        {
            "login": "login_23",
            "roles": [UserRole.guest, UserRole.player],
        }
    ))
