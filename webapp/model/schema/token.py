from datetime import datetime

from pydantic import BaseModel


class RefreshTokenPayload(BaseModel):
    sub: str
    nbf: datetime
    exp: datetime


class AccessTokenPayload(RefreshTokenPayload):
    iss: str


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    # pass