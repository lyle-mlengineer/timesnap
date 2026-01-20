from fastapi import FastAPI, status

from contextlib import asynccontextmanager
import logging

from app.v1.core.config import config
from app.v1.core.logging import setup_logging

from app.v1.main_helpers import setup_app

setup_logging()

logging.info("Starting application...")
logging.info(f"Environment: {config.ENVIRONMENT}")

if config.ENVIRONMENT == "production":
    logging.warning("Running in production mode")

@asynccontextmanager
async def lifespan(app: FastAPI):
    logging.info("Starting application...")
    # init_app(app)
    yield

app = FastAPI(
    title=config.APP_NAME, 
    debug=config.DEBUG, 
    lifespan=lifespan, 
    summary=config.APP_SUMMARY,
    description=config.APP_DESCRIPTION,
    version=config.APP_VERSION,
    contact={"name": config.APP_CONTACT_NAME}
)

setup_app(app)

@app.get(
        "/health", 
        status_code=status.HTTP_200_OK, 
        response_model=dict, 
        tags=["Health"],
        summary="Health check",
        description="Health check",
        response_description="Health check"
        )
async def health_check():
    logging.info("Health check")
    return {"status": "ok"}

@app.get("/test", status_code=status.HTTP_200_OK, tags=["Test"], summary="Test", description="Test", response_description="Test")
async def test_endpoint():
    import requests

    url: str = config.GENERATION_API_URL
    logging.info(f"Calling ML service at {url}")
    response = requests.get(url)
    logging.info(f"ML service response: {response.json()}")
    return {"message": "Test successful"}

logging.info("Application started successfully.")