import jwt

from ..core.config import env_config
from ..exception.auth import CredentialException


class JWTValidator:
    def __init__(self, _token_conf):
        self._token_conf = _token_conf

    def get_user_uuid(self, token: str):
        payload = jwt.decode(token,
                             self._token_conf.secret_key,
                             algorithms=[self._token_conf.algorithm])
        user_uuid = payload.get("sub")
        if user_uuid:
            return user_uuid
        raise CredentialException


access_token_validator = JWTValidator(env_config.security.access_token)
refresh_token_validator = JWTValidator(env_config.security.refresh_token)

# def get_user_uuid(access_token:str):
#     jwt.decode(access_token,algorithms=[]
