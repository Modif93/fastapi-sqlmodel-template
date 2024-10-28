# TODO: 포럼글 작성 스키마 만들기
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ForumRequest(BaseModel):
    title: str
    content: str


class ForumResponse(ForumRequest):
    id: int
    reg_dt: Optional[datetime]
    mod_dt: Optional[datetime]


class ForumPostRequest(ForumRequest):
    pass


class ForumPostResponse(ForumPostRequest):
    id: int
    reg_dt: Optional[datetime]
    mod_dt: Optional[datetime]
