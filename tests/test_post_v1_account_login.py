from services.dm_api_account import Facade
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
    api = Facade(host='http://localhost:5051')
    api.login.login_user(login="login_23", password="login_23", remember_me=True)
