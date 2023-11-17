import time

from generic.helpers.dm_db import DmDatabase
from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    db = DmDatabase(user='postgres', password='admin', host='localhost', database='dm3.5')
    api = Facade(host='http://localhost:5051')
    login = "login_46"
    email = "login_46@mail.ru"
    password = "login_46"

    # Delete user
    db.delete_user_by_login(login)
    dataset = db.get_user_by_login(login=login)
    assert len(dataset) == 0

    api.mailhog.delete_all_messages()

    # Register new user
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f'User {login} not registered'
        assert row['Activated'] is False, f'User {login} is activated'

    # Activate registered user in Database

    db.activate_user_by_login(login=login)
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f'User {login} not registered'
        assert row['Activated'] is True, f'User {login} is activated'

    # Activate registered user
    api.account.activate_registered_user(login=login)
    time.sleep(2)
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f'User {login} is not activated'

