from services.dm_api_account import Facade
import structlog
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    api = Facade(host='http://localhost:5051')
    login = 'login_25'
    password = 'login_25'
    token = api.login.get_auth_token(login=login, password=password)
    api.account.set_headers(headers=token)
    api.login.set_headers(headers=token)
    # api.account.get_current_user_info(headers=token)
    api.account.get_current_user_info()
    api.login.logout_user()
