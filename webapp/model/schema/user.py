from typing import Optional
from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    username: str
    email: Optional[str] = Field(default=None)
    full_name: Optional[str] = Field(default=None)
    disabled: Optional[bool] = Field(default=None)
    user_level: Optional[int] = Field(default=None)


class UserRequest(UserResponse):
    hashed_password: str
