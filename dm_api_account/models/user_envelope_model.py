from typing import List, Optional

from pydantic import BaseModel, StrictStr, Field, StrictBool, ConstrainedDate
from enum import Enum


class Roles(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMINISTRATOR = 'Administrator'
    NANNY_MODERATOR = 'NannyModerator'
    REGULAR_MODERATOR = 'RegularModerator'
    SENIOR_MODERATOR = 'SeniorModerator'


class Rating(BaseModel):
    enabled: StrictBool
    quality: int
    quantity: int


class User(BaseModel):
    login: Optional[StrictStr]
    roles: Optional[List[Roles]]
    medium_picture_url: Optional[StrictStr] = Field(alias="mediumPictureUrl")
    small_picture_url: Optional[StrictStr] = Field(alias="smallPictureUrl")
    status: Optional[StrictStr]
    rating: Optional[Rating]
    online: Optional[ConstrainedDate]
    name: Optional[StrictStr]
    location: Optional[StrictStr]
    registration: Optional[ConstrainedDate]


class UserEnvelopeModel(BaseModel):
    resource: Optional[User]
    metadata: Optional[StrictStr]
