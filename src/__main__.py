from uvicorn import run as run_fastapi

from core.create_app import create_app
from core.settings.base_settings import settings

if __name__ == "__main__":
    run_fastapi(create_app(), host=settings.host)
