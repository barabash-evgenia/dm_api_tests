from requests import Response
from ..models.login_credentials_model import LoginCredentialsModel
from restclient.restclient import Restclient
from ..models.user_envelope_model import UserEnvelopeModel


class LoginApi:

    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.client = Restclient(host=host, headers=headers)
        self.client.session.headers.update(headers) if headers else None

    def post_v1_account_login(self, json: LoginCredentialsModel, **kwargs) -> Response:
        """
        :param json: login_credentials_model
        Authenticate via credentials
        :return:
        """
        response = self.client.post(
            path="/v1/account/login",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        # UserEnvelopeModel(**response.json())
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
