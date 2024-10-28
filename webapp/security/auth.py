import uuid
import jwt
from datetime import datetime, timedelta, timezone
from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from argon2 import PasswordHasher

from ..core.configuration import env_config
from ..exception.auth import LoginException
from ..model.schema.user import UserResponse
from ..service.user import UserService

loginForm = Annotated[OAuth2PasswordRequestForm, Depends()]
tokenHeader = Annotated[str, Depends(OAuth2PasswordBearer(tokenUrl="auth"))]
userService = Annotated[UserService, Depends(UserService)]


class Authenticate(object):
    def __init__(self, user_service: userService):
        self.hashing = PasswordHasher()
        self.user_service = user_service
        self.tokenize_conf = env_config.security.tokenize

    def _get_password_hash(self, password):
        return self.hashing.hash(password)

    def _verify_password(self, plain_password, hashed_password):
        return self.hashing.verify(plain_password, hashed_password)

    def _get_user(self, username):
        user_db = self.user_service.get_user_by_id(username)
        if user_db:
            return user_db

    def authenticate_user(self, username: str, password: str):
        user = self._get_user(username)
        if not user:
            raise LoginException("id")
        if not self._verify_password(password, user.hashed_password):
            raise LoginException("pw")
        return user

    def create_access_token(self, current_dt, user: UserResponse):
        access_token_expires = current_dt + timedelta(minutes=self.tokenize_conf.expire_min)

        access_token_data = {
            "sub": user.username,
            "nbf": datetime.now(timezone.utc),
            "exp": access_token_expires,
            "jti": str(uuid.uuid4())
        }

        return jwt.encode(
            access_token_data, self.tokenize_conf.secret_key, algorithm=self.tokenize_conf.algorithm)

    def create_refresh_token(self, current_dt, user: UserResponse):
        refresh_token_expires = current_dt + timedelta(hours=self.tokenize_conf.refresh_hours)
        refresh_token_data = {
            "sub": user.username,
            "exp": refresh_token_expires,
        }
        return jwt.encode(
            refresh_token_data, self.tokenize_conf.refresh_secret_key,
            algorithm=self.tokenize_conf.algorithm)
