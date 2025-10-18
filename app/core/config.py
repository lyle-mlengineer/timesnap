from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    app_name: str = "TimeSnap"
    debug: bool = False
    db_user: str = ""
    db_password: str = ""
    db_name: str = "test.db"

    templates_dir: str = "app/ui/v1/templates"
    static_dir: str = "app/ui/v1/static"

    YOUTUBE_CREDENTIALS_PATH: str = os.getenv(
        "YOUTUBE_CREDENTIALS_PATH", "credentials.json"
    )
    CLIENT_SECRET_FILE: str = os.environ.get(
        "CLIENT_SECRET_FILE", "C:/Users/Computer Forensics/Downloads/secret.json"
    )
    DATA_DIR: str = os.environ.get("DATA_DIR", os.path.join("C:/Users/Computer Forensics/Desktop/Git/timesnap", "data"))

    @property
    def db_url(self):
        return f"sqlite:///./{self.db_name}"


config = Config()
