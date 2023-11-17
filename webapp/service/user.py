"""User Service module."""

from uuid import uuid4
from typing import Annotated, Sequence

from fastapi import Depends
from ..repository.user import UserRepository
from ..model.user import User


class UserService(object):
    def __init__(
            self,
            _repository: Annotated[UserRepository, Depends(UserRepository)]):
        self._repository = _repository

    def get_users(self) -> Sequence[User]:
        return self._repository.get_all()

    def get_user_by_id(self, user_id: int) -> User:
        return self._repository.get_by_id(user_id)

    def create_user(self) -> User:
        uid = uuid4()
        return self._repository.add(email=f"{uid}@email.com", password="pwd")

    def delete_user_by_id(self, user_id: int) -> None:
        return self._repository.delete_by_id(user_id)
