from services.dm_api_account import Facade
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_1():
    api = Facade(host='http://localhost:5051')
    login = "login_41"
    email = "login_41@mail.ru"
    password = "login_41"
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)
    token = api.login.get_auth_token(login=login, password=password)
    api.account.set_headers(headers=token)
    api.login.set_headers(headers=token)
    api.account.get_current_user_info()
    api.login.logout_user()


def test_2():
    api = Facade(host='http://localhost:5051')
    login = "login_42"
    email = "login_42@mail.ru"
    password = "login_42"
    api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )
    api.account.activate_registered_user(login=login)
    token = api.login.get_auth_token(login=login, password=password)
    api.account.get_current_user_info(headers=token)
    api.login.logout_user(headers=token)
