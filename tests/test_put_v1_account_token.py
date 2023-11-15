from services.dm_api_account import DmApiAccount
import structlog
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = DmApiAccount(host='http://localhost:5051')
    response = api.account.put_v1_account_token(token="915ec48a-107b-416a-9d07-bd91902c7df7", status_code=200)
    assert_that(response.resource, has_properties(
        {
            "login": "login_25",
            "roles": [UserRole.guest, UserRole.player],
        }
    ))
