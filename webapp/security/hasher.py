from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from ..core.config import env_config


class Hasher:
    def __init__(self):
        hashing_config = env_config.security.hashing
        if hashing_config:
            self.hasher = PasswordHasher(**hashing_config.model_dump(exclude_none=True))
        else:
            self.hasher = PasswordHasher()

    def print_hasher(self):
        print(f"time_cost: {self.hasher.time_cost}")
        print(f"memory_cost: {self.hasher.memory_cost}")
        print(f"parallelism: {self.hasher.parallelism}")
        print(f"hash_len: {self.hasher.hash_len}")
        print(f"salt_len: {self.hasher.salt_len}")

    def hash_password(self, password):
        return self.hasher.hash(password)

    def verify_password(self, password, hashed_password):
        try:
            return self.hasher.verify(hashed_password, password)
        except VerifyMismatchError:
            return False


hasher = Hasher()


