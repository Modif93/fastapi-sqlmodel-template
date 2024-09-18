from sqlmodel import SQLModel, Field
from sqlalchemy import Column, String


class User(SQLModel, table=True):
    __tablename__ = "tbl_user"

    username: str = Field(sa_column=Column(String(50), primary_key=True))
    email: str = Field(sa_column=Column(String(50), unique=True))
    full_name: str = Field(sa_column=Column(String(50), default=None))
    disabled: bool = Field(sa_column=Column(String(50), default=False))
    user_level: int = Field(sa_column=Column(String(50), default=5))
    hashed_password: str = Field(sa_column=Column(String(100)))
