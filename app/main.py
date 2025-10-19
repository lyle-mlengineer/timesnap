from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.v1 import user
from app.api.v1 import extraction
from app.ui.v1 import ui
from app.api.v1 import api_keys
from app.core.config import config
from app.core.logging import setup_logging
from app.db.schema import Base, engine

setup_logging()
Base.metadata.create_all(bind=engine)

app = FastAPI(title=config.app_name)


# Register routes
app.include_router(user.router, prefix="/api/v1")
app.include_router(ui.router)
app.include_router(extraction.router)
app.include_router(api_keys.router)

# Mount static folder
app.mount("/static", StaticFiles(directory=config.static_dir), name="static")
app.mount("/data", StaticFiles(directory=config.DATA_DIR), name="data")
