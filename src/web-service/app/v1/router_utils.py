from fastapi import status, Request
from fastapi.responses import RedirectResponse

from app.v1.core.config import config


def create_redirect_response(
        request: Request, 
        redirect_url: str, 
        cookie_value: str, 
        cookie_key: str,
        max_age: int
    ) -> RedirectResponse:
    response = RedirectResponse(url=request.url_for(redirect_url), status_code=status.HTTP_302_FOUND)
    response.set_cookie(
        key=cookie_key, 
        value=cookie_value, 
        httponly=config.HTTP_ONLY, 
        samesite=config.SAMESITE, 
        max_age=max_age
    )
    return response