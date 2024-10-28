from datetime import datetime, timezone
from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestFormStrict
from ..model.schema.token import Token
from ..service.login import LoginService

router = APIRouter()

login_form = Annotated[OAuth2PasswordRequestFormStrict, Depends()]
login_service = Annotated[LoginService, Depends()]
# token_header = Annotated[]

@router.post("/token", summary="로그인")
def generate_token(
        form_data: login_form,
        _login_service: login_service,
        # user_security: userSecurity
) -> Token:
    """토큰을 발급합니다."""
    return _login_service.generate_token(form_data.username, form_data.password)

@router.get("/token", summary="토큰 재발급")
def refresh_token(
        # token_data:
        _refresh_token: token_header,
        _login_service: login_service,
) -> Token:
    return _login_service.refresh_token(_refresh_token)