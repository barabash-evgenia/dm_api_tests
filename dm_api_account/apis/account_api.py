from requests import Response
from ..models.registration_model import RegistrationModel
from ..models.change_email_model import ChangeEmailModel
from ..models.change_password_model import ChangePasswordModel
from restclient.restclient import Restclient
from ..models.user_envelope_model import UserEnvelopeModel
from ..models.user_details_envelope_model import UserDetailsEnvelopeModel
from ..models.reset_password_model import ResetPasswordModel


class AccountApi:
    def __init__(self, host, headers=None):
        self.host = host
        self.headers = headers
        self.client = Restclient(host=host, headers=headers)
        self.client.session.headers.update(headers) if headers else None

    def post_v1_account(self, json: RegistrationModel, **kwargs) -> Response:
        """
        :param json: registration_model
        Register new user
        :return:
        """
        response = self.client.post(
            path="/v1/account/",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        return response

    def post_v1_account_password(self, json: ResetPasswordModel, **kwargs) -> Response:
        """
        :param json: reset_password_model
        Reset registered user password
        :return:
        """
        response = self.client.post(
            path="/v1/account/password",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_email(self, json: ChangeEmailModel, **kwargs) -> Response:
        """
        :param json: change_email_model
        Change registered user email
        :return:
        """
        response = self.client.put(
            path="/v1/account/email",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        UserEnvelopeModel(**response.json())
        return response

    def put_v1_account_password(self, json: ChangePasswordModel, **kwargs) -> Response:
        """
        :param json: change_password_model
        Change registered user password
        :return:
        """
        response = self.client.put(
            path="/v1/account/password",
            json=json.dict(by_alias=True, exclude_none=True),
            **kwargs
        )
        # UserEnvelopeModel(**response.json())
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
        UserEnvelopeModel(**response.json())
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
        UserDetailsEnvelopeModel(**response.json())
        return response
