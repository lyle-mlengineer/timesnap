from dotenv import load_dotenv
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

    @property
    def db_url(self):
        return f"sqlite:///./{self.db_name}"


config = Config()
