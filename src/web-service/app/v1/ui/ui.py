from fastapi import status
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

import logging

from app.v1.core.config import config

templates = Jinja2Templates(directory=config.TEMPLATES_DIR)

router = APIRouter(
    tags=["User Interface"],)


@router.get('/', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def get_landing_page(request: Request):
    """Load the home page"""
    logging.info("Loading landing page")
    return templates.TemplateResponse(
        "landing_page.html", 
        {
            "request": request,
        }
    )