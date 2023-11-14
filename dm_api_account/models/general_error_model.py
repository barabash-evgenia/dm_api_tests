from typing import Optional

from pydantic import BaseModel, StrictStr


class GeneralErrorModel(BaseModel):
    message: Optional[StrictStr]
