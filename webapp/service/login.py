from typing import Annotated
from datetime import datetime, timezone
from fastapi import Depends
from ..model.schema.token import Token
from ..model.db.user import User
from ..repository.user import UserRepository
from ..security.pw_hash import hashing_module
from ..security.jwt_issue import access_token_issuer, refresh_token_issuer
from ..security.jwt_valid import refresh_token_validator, access_token_validator
from ..exception.auth import LoginException, CredentialException

user_repository = Annotated[UserRepository, Depends()]


class UserRedisRepository:
    pass


user_redis_repository = Annotated[UserRedisRepository, Depends()]


class LoginService(object):
    def __init__(self, _user_repository: user_repository):
        self._user_repository = _user_repository

    def generate_token(self, username, password):
        current_dt = datetime.now(timezone.utc)
        user: User = self._user_repository.get_by_username(username)
        if user and hashing_module.verify_password(password, user.hashed_password):
            return Token(
                access_token=access_token_issuer.create_token(current_dt, user),
                refresh_token=refresh_token_issuer.create_token(current_dt, user),
                token_type="bearer")
        raise LoginException

    def refresh_token(self, refresh_token):
        current_dt = datetime.now(timezone.utc)
        user: User = self._user_repository.get_by_uuid(
            refresh_token_validator.get_user_uuid(refresh_token))
        if user:
            return Token(
                access_token=access_token_issuer.create_token(current_dt, user),
                refresh_token=refresh_token,
                token_type="bearer")

        raise CredentialException

    def get_user_from_token(self, access_token):
        user: User = self._user_repository.get_by_uuid(
            access_token_validator.get_user_uuid(access_token))
        if user:
            return user

        raise CredentialException
