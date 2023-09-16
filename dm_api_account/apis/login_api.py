from requests import Response
from ..models.login_credentials_model import login_credentials_model
from restclient.restclient import Restclient


class LoginApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.client = Restclient(host=host, headers=headers)
        self.client.session.headers.update(headers) if headers else None

    def post_v1_account_login(self, json: login_credentials_model, **kwargs) -> Response:
        """
        :param json: login_credentials_model
        Authenticate via credentials
        :return:
        """
        response = self.client.post(
            path="/v1/account/login",
            json=json,
            **kwargs
        )
        return response

    def delete_v1_account_login(self, **kwargs) -> Response:
        """
        Logout as current user
        :return:
        """
        response = self.client.delete(
            path="/v1/account/login",
            **kwargs
        )
        return response

    def delete_v1_account_login_all(self, **kwargs) -> Response:
        """
        Logout from every device
        :return:
        """
        response = self.client.delete(
            path="/v1/account/login/all",
            **kwargs
        )
        return response
