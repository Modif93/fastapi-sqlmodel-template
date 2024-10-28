__all__ = (
    "SUPER_ADMIN",
    "ADMIN",
    "MOD",
    "EMAIL_VERIFIED",
    "TEMPORARY",
)

SUPER_ADMIN = 0
ADMIN = 1
MOD = 2
USER = 3
EMAIL_VERIFIED = 4
TEMPORARY = 5


def __dir__() -> list[str]:
    return sorted(list(__all__))  # pragma: no cover
