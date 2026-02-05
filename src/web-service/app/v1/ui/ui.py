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

@router.get('/login', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def get_login_page(request: Request):
    """Load the login page"""
    logging.info("Loading login page")
    return templates.TemplateResponse(
        "oauth.html", 
        {
            "request": request,
            "title": "Login"
        } 
    )

@router.get('/user_dashboard', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def get_user_dashboard(request: Request):
    """Load the user dashboard"""
    logging.info("Loading user dashboard")
    return templates.TemplateResponse(
        "user_dashboard.html", 
        {
            "request": request,
            "title": "User Dashboard"
        } 
    )

@router.get('/extract', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def get_extract_timestamps(request: Request):
    """Load the extract timestamps page"""
    logging.info("Loading extract timestamps page")
    return templates.TemplateResponse(
        "extract_timestamps.html", 
        {
            "request": request,
            "title": "Extract Timestamps",
            "page": "extract"
        } 
    )

@router.get('/purchase_credits', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def get_purchase_credits(request: Request):
    """Load the purchase credits page"""
    logging.info("Loading purchase credits page")
    return templates.TemplateResponse(
        "purchase_credits.html", 
        {
            "request": request,
            "title": "Purchase Credits"
        } 
    )

@router.get('/api_keys', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def get_api_keys(request: Request):
    """Load the api keys page"""
    logging.info("Loading api keys page")
    return templates.TemplateResponse(
        "api_keys.html", 
        {
            "request": request,
            "title": "API Keys"
        } 
    )

@router.get("/payment_providers", status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def get_payment_providers(request: Request):
    """Load the payment providers page"""
    logging.info("Loading payment providers page")
    return templates.TemplateResponse(
        "payment_providers.html", 
        {
            "request": request,
            "title": "Payment Providers"
        } 
    )

@router.get('/settings', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def get_settings(request: Request):
    """Load the settings page"""
    logging.info("Loading settings page")
    return templates.TemplateResponse(
        "settings.html", 
        {
            "request": request,
            "title": "Settings"
        } 
    )

@router.get('/profile', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def get_profile(request: Request):
    """Load the profile page"""
    logging.info("Loading profile page")
    return templates.TemplateResponse(
        "profile.html", 
        {
            "request": request,
            "title": "Profile"
        } 
    )

@router.get('/notifications', status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def get_notifications(request: Request):
    """Load the notifications page"""
    logging.info("Loading notifications page")
    return templates.TemplateResponse(
        "notifications.html", 
        {
            "request": request,
            "title": "Notifications"
        } 
    )