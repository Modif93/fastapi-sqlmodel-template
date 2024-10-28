from datetime import datetime
from typing import Optional, TYPE_CHECKING

from sqlmodel import (SQLModel, Field, Relationship, Column,
                      Integer, BigInteger,
                      String, Text, DateTime)

from .common import Audit

if TYPE_CHECKING:
    from .user import User


class Forum(Audit):
    __tablename__ = "tbl_forum"

    id: Optional[int] = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    name: str = Field(sa_column=Column(String(300)))
    description: str = Field(sa_column=Column(Text))

    posts: Optional['ForumPosts'] = Relationship(back_populates="forum")


class ForumPosts(Audit):
    __tablename__ = "tbl_forum_posts"

    id: Optional[int] = Field(sa_column=Column(BigInteger, primary_key=True, autoincrement=True))
    user_id: Optional[int] = Field(foreign_key='tbl_user.id')
    forum_id: Optional[int] = Field(foreign_key='tbl_forum.id')
    title: str = Field(sa_column=Column(String(300)))
    content: str = Field(sa_column=Column(Text))

    user: Optional['User'] = Relationship(back_populates="forum")
    forum: Optional[Forum] = Relationship(back_populates="posts")
