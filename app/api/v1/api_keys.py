from typing import Annotated

from fastapi import APIRouter, Form, Request, status
from fastapi.responses import RedirectResponse

router = APIRouter(tags=["API Keys"], prefix="/api_keys")


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_api_key(name: Annotated[str, Form()], request: Request):
    # Logic to create an API key would go here
    return RedirectResponse(url=request.url_for("get_api_keys_page"), status_code=status.HTTP_303_SEE_OTHER)