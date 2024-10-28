from datetime import datetime

from pydantic import BaseModel


class RefreshToken(BaseModel):
    sub: str
    nbf: datetime
    exp: datetime


class AccessToken(RefreshToken):
    iss: str
