from fastapi import HTTPException, status


class LoginException(HTTPException):
    def __init__(self, _type):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Incorrect username or password {_type}",
            headers={"WWW-Authenticate": "Bearer"},
        )


class CredentialException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
