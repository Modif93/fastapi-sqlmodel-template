from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from ..core.config import env_config


class HashingModule:
    def __init__(self):
        hashing_config = env_config.security.hashing
        if hashing_config:
            self._hasher = PasswordHasher(**hashing_config.model_dump(exclude_none=True))
        else:
            self._hasher = PasswordHasher()

    def print_hasher(self):
        print(f"time_cost: {self._hasher.time_cost}")
        print(f"memory_cost: {self._hasher.memory_cost}")
        print(f"parallelism: {self._hasher.parallelism}")
        print(f"hash_len: {self._hasher.hash_len}")
        print(f"salt_len: {self._hasher.salt_len}")

    def hash_password(self, password):
        return self._hasher.hash(password)

    def verify_password(self, password, hashed_password):
        try:
            return self._hasher.verify(hashed_password, password)
        except VerifyMismatchError:
            return False


hashing_module = HashingModule()


