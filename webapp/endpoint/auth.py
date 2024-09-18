from datetime import datetime, timezone
from typing import Annotated

from fastapi import APIRouter, Depends

from ..model.schema.system import Token
from ..security.user import UserSecurity, loginForm

router = APIRouter(tags=['시스템 관리'])

userSecurity = Annotated[UserSecurity, Depends(UserSecurity)]


@router.post("/auth", summary="로그인")
async def login_for_access_token(
        form_data: loginForm,
        user_security: userSecurity
) -> Token:
    """토큰을 발급합니다."""
    current_dt = datetime.now(timezone.utc)
    user = user_security.authenticate_user(form_data.username, form_data.password)
    access_token = user_security.create_access_token(current_dt, user)
    refresh_token = user_security.create_refresh_token(current_dt, user)
    return Token(access_token=access_token, token_type="bearer")
