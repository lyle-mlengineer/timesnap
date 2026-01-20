from dotenv import load_dotenv
from pydantic_settings import BaseSettings

import os

load_dotenv()


class Config(BaseSettings):
    ENVIRONMENT: str = os.environ.get("ENVIRONMENT", "development")
    DEBUG: bool = os.environ.get("DEBUG", True)

    APP_NAME: str = os.environ.get("APP_NAME", "Savannah Faces ML Service")
    APP_VERSION: str = os.environ.get("APP_VERSION", "0.1.0")
    API_VERSION: str = os.environ.get("API_VERSION", "v1")
    APP_SUMMARY: str = os.environ.get("APP_SUMMARY", "API for Savannah Faces ML Service")
    APP_DESCRIPTION: str = os.environ.get("APP_DESCRIPTION", "This is the API for Savannah Faces ML Service, which provides image generation services.")
    APP_CONTACT_NAME: str = os.environ.get("APP_CONTACT_NAME", "Lyle")

    IMAGES_DIR: str = os.environ.get("IMAGES_DIR", f"app/{API_VERSION}/data/images")

    GOOGLE_DRIVE_FOLDER_ID: str = os.environ["GOOGLE_DRIVE_FOLDER_ID"]
    GOOGLE_DRIVE_CREDENTIALS: str = os.environ["GOOGLE_DRIVE_CREDENTIALS"]

config = Config()