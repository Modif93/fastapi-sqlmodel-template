from typing import TYPE_CHECKING, Optional, List

from sqlmodel import SQLModel, Field, Relationship, Column, Integer, String

if TYPE_CHECKING:
    from .forum import ForumPosts


class User(SQLModel, table=True):
    __tablename__ = "tbl_user"

    id: Optional[int] = Field(sa_column=Column(Integer, primary_key=True, autoincrement=True))
    username: str = Field(sa_column=Column(String(50), unique=True))
    email: str = Field(sa_column=Column(String(50), unique=True))
    full_name: str = Field(sa_column=Column(String(50), default=None))
    disabled: bool = Field(sa_column=Column(String(50), default=False))
    user_level: int = Field(sa_column=Column(String(50), default=5))
    hashed_password: str = Field(sa_column=Column(String(100)))
    user_uuid: str = Field(sa_column=Column(String(50), unique=True))

    forum_posts: List['ForumPosts'] = Relationship(back_populates="user")
