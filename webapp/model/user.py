"""User Models module."""

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"

    username: int = Field(primary_key=True)
    email: str = Field(unique=True)
    full_name: str | None = None
    hashed_password: str
    is_active: bool
