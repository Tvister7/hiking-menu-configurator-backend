import os
import sys

from fastapi.applications import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from .api.app_status import status_router
from .api.views.meal import meal_router

app = FastAPI(
    title="Hiking menu",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    version=os.getenv("APP_VERSION", default="DEV"),
)

logger_config = {
    "handlers": [
        {
            "sink": sys.stdout,
            "format": "<level>{level}: {function: ^15} - {line: >3}: {message}</level>",  # noqa
        }
    ]
}


def create_app():
    logger.configure(**logger_config)
    app.include_router(status_router)
    app.include_router(meal_router, prefix="/api/base")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
