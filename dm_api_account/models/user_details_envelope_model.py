from typing import List, Optional

from pydantic import BaseModel, StrictStr, StrictInt, Field, StrictBool, ConstrainedDate
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


class ParseMode(Enum):
    COMMON = 'Common'


class ColorSchema(Enum):
    MODERN = 'Modern'


class Info(BaseModel):
    value: StrictStr
    parseMode: Optional[List[ParseMode]]


class Paging(BaseModel):
    posts_per_page: Optional[StrictInt] = Field(alias="postsPerPage")
    comments_per_page: Optional[StrictInt] = Field(alias="commentsPerPage")
    topics_per_page: Optional[StrictInt] = Field(alias="topicsPerPage")
    messages_per_page: Optional[StrictInt] = Field(alias="messagesPerPage")
    entities_per_page: Optional[StrictInt] = Field(alias="entitiesPerPage")


class Settings(BaseModel):
    color_schema: Optional[List[ColorSchema]] = Field(alias="colorSchema")
    nanny_greetings_message: Optional[StrictStr] = Field(alias="nannyGreetingsMessage")


class UserDetails(BaseModel):
    login: Optional[StrictStr]
    roles: Optional[List[ParseMode]]
    medium_picture_url: Optional[StrictStr] = Field(alias="mediumPictureUrl")
    small_picture_url: Optional[StrictStr] = Field(alias="smallPictureUrl")
    status: Optional[StrictStr]
    rating: Optional[Rating]
    online: Optional[ConstrainedDate]
    name: Optional[StrictStr]
    location: Optional[StrictStr]
    registration: Optional[ConstrainedDate]
    icq: Optional[StrictStr]
    skype: Optional[StrictStr]
    original_picture_url: Optional[StrictStr] = Field(alias="originalPictureUrl")
    info: Optional[Info]
    settings: Optional[Settings]


class UserDetailsEnvelopeModel(BaseModel):
    resource: Optional[UserDetails]
    metadata: Optional[StrictStr]
