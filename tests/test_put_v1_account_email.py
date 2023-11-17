from services.dm_api_account import Facade
import structlog
from dm_api_account.models.change_email_model import ChangeEmail
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_email():
    api = Facade(host='http://localhost:5051')
    json = ChangeEmail(
        login="login_24",
        email="login_24444@mail.ru",
        password="login_24"
    )
    response = api.account_api.put_v1_account_email(json=json, status_code=200)
    assert_that(response.resource, has_properties(
        {
            "login": "login_24",
            "roles": [UserRole.guest, UserRole.player],
        }
    ))
