import uuid
from datetime import timedelta, datetime, timezone

import jwt

from ..model.db.user import User
from ..model.schema.token import AccessTokenPayload, RefreshTokenPayload
from ..core.config import env_config, TokenConfig


class JWTIssuer(object):
    def __init__(self, _token_conf: TokenConfig):
        self._token_conf = _token_conf
        # self.refresh_token_conf = env_config.security.refresh_token

    def create_token(self, current_dt: datetime, user: User):
        token = AccessTokenPayload(
            iss=self._token_conf.issuer,
            sub=user.user_uuid,
            nbf=datetime.now(timezone.utc),
            exp=current_dt + timedelta(minutes=self._token_conf.expire_min)
        )
        access_token_data = token.model_dump(exclude_none=True)

        return jwt.encode(
            access_token_data, self._token_conf.secret_key, algorithm=self._token_conf.algorithm)


access_token_issuer = JWTIssuer(env_config.security.access_token)
refresh_token_issuer = JWTIssuer(env_config.security.refresh_token)
