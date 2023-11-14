from pydantic import BaseModel, StrictStr


class ChangeEmailModel(BaseModel):
    login: StrictStr
    password: StrictStr
    email: StrictStr

# change_email_model = {
#     "login": "login_114",
#     "password": "login_114",
#     "email": "login_444@mail.ru"
# }
