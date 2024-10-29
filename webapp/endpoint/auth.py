from typing import Annotated

import httpx
from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
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


@router.get('/naverlogin')
def get_naver_login():
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    state = "RAMDOM_STATE"
    redirectURI = "YOUR_CALLBACK_URL"


    base_url = "https://nid.naver.com/oauth2.0/authorize"
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirectURI,
        "state": state
    }

    api_url = httpx.URL(base_url).copy_merge_params(params)

    return HTMLResponse(
        f"<a href='{api_url}'><img height='50' src='http://static.nid.naver.com/oauth/small_g_in.PNG'/></a>",
        200, {'Content-Type': 'text/html;charset=utf-8'})


if __name__ == "__main__":
    base_url = "https://example.com/api"
    params = {
        "search": "python 함수",
        "page": 2,
        "sort": "asc"
    }
