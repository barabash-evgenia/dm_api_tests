from requests import Response
from ..models.registration_model import registration_model
from ..models.reset_password_model import reset_password_model
from ..models.change_email_model import change_email_model
from ..models.change_password_model import change_password_model
from restclient.restclient import Restclient


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.client = Restclient(host=host, headers=headers)
        self.client.session.headers.update(headers) if headers else None

    def post_v1_account(self, json: registration_model, **kwargs) -> Response:
        """
        :param json: registration_model
        Register new user
        :return:
        """
        response = self.client.post(
            path="/v1/account/",
            json=json,
            **kwargs
        )
        return response

    def post_v1_account_password(self, json: reset_password_model, **kwargs) -> Response:
        """
        :param json: reset_password_model
        Reset registered user password
        :return:
        """
        response = self.client.post(
            path="/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_email(self, json: change_email_model, **kwargs) -> Response:
        """
        :param json: change_email_model
        Change registered user email
        :return:
        """
        response = self.client.put(
            path="/v1/account/email",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_password(self, json: change_password_model, **kwargs) -> Response:
        """
        :param json: change_password_model
        Change registered user password
        :return:
        """
        response = self.client.put(
            path="/v1/account/password",
            json=json,
            **kwargs
        )
        return response

    def put_v1_account_token(self, token: str, **kwargs) -> Response:
        """
        Activate registered user
        :return:
        """
        response = self.client.put(
            path=f"/v1/account/{token}",
            **kwargs
        )
        return response

    def get_v1_account(self, **kwargs) -> Response:
        """
        Get current user
        :return:
        """
        response = self.client.get(
            path="/v1/account",
            **kwargs
        )
        return response
