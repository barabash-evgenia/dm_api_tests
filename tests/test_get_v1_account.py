from services.dm_api_account import DmApiAccount
import structlog
from hamcrest import assert_that, has_properties
from dm_api_account.models.user_envelope_model import UserRole

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    api = DmApiAccount(host='http://localhost:5051', headers={
        'X-Dm-Auth-Token': 'IQJh+zgzF5DAdTdJZYMSq3R9bl4CKSMEV7m7ugTLKStOQZk8aUjJGgc67gkJbrqQbXaVqF9WOCt51pacJ3msFOnG0qlsiWHtakvKqf96yyrDVwiouhpLmTuVI7ioU6X2QfmkzA4Mg74= '})
    response = api.account.get_v1_account()
    assert_that(response.resource, has_properties(
        {
            "login": "login_25",
            "roles": [UserRole.guest, UserRole.player],
        }
    ))
