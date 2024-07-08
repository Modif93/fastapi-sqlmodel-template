"""User Repository module."""

from typing import Sequence, Type

from sqlmodel import select

from ..core.repository import Repository
from ..exception.entity import EntityNotFoundError
from ..model.user import User


class UserRepository(Repository):
    _model: User
    _entity_name: "User"