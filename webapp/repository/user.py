"""User Repository module."""

from typing import Sequence, Type

from sqlmodel import select

from ..core.abstract import RepositoryABC
from ..exception.entity import EntityNotFoundError
from ..model.user import User


class UserRepository(RepositoryABC):

    def get_all(self) -> Sequence[User]:
        return self._session.scalars(select(User)).all()

    def get_by_id(self, _id: int) -> User:
        entity = self._session.get(User, _id)
        if not entity:
            raise UserNotFoundError(_id)
        return entity

    def add(self, email: str, password: str, is_active: bool = True) -> User:
        user = User(email=email, hashed_password=password, is_active=is_active)
        self._session.add(user)
        self._session.commit()
        self._session.refresh(user)
        return user

    def delete_by_id(self, _id: int) -> None:
        entity = self._session.get(User, _id)
        if not entity:
            raise UserNotFoundError(_id)
        self._session.delete(entity)
        self._session.commit()


class UserNotFoundError(EntityNotFoundError):
    entity_name: str = "User"