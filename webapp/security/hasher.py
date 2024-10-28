from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from ..core.configuration import env_config


class Hasher:
    def __init__(self):
        hashing_config = env_config.security.hashing
        if hashing_config:
            self.hasher = PasswordHasher(**hashing_config.model_dump(exclude_none=True))
        else:
            self.hasher = PasswordHasher()

    def hash_password(self, password):
        return self.hasher.hash(password)

    def verify_password(self, password, hashed_password):
        try:
            return self.hasher.verify(hashed_password, password)
        except VerifyMismatchError:
            return False
