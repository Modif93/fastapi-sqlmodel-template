import uuid
from datetime import timedelta, datetime, timezone

import jwt

from ..model.db.user import User
from ..core.configuration import env_config


class JWTIssuer(object):

    def __init__(self):
        self.tokenize_conf = env_config.security.tokenize

    def create_access_token(self, current_dt, user: User):
        access_token_expires = current_dt + timedelta(minutes=self.tokenize_conf.expire_min)

        access_token_data = {
            "sub": user.username,
            "nbf": datetime.now(timezone.utc),
            "exp": access_token_expires,
            "jti": str(uuid.uuid4())
        }

        return jwt.encode(
            access_token_data, self.tokenize_conf.secret_key, algorithm=self.tokenize_conf.algorithm)

    def create_refresh_token(self, current_dt, user: User):
        refresh_token_expires = current_dt + timedelta(hours=self.tokenize_conf.refresh_hours)
        refresh_token_data = {
            "sub": user.username,
            "exp": refresh_token_expires,
        }
        return jwt.encode(
            refresh_token_data, self.tokenize_conf.refresh_secret_key,
            algorithm=self.tokenize_conf.algorithm)