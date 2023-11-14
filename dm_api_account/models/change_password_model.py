from pydantic import BaseModel, StrictStr, Field


class ChangePasswordModel(BaseModel):
    login: StrictStr
    token: StrictStr
    # old_password: StrictStr = Field(alias="oldPassword")
    # new_password: StrictStr = Field(alias="newPassword")
    old_password: StrictStr
    new_password: StrictStr
