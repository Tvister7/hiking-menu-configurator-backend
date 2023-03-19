import os
import sys

from fastapi.applications import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from core.external.postgres import create_db_and_tables

from .api.app_status import status_router
from .api.views.meal import meal_router
from .api.views.user import Routers

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

    app.include_router(Routers.auth_router, prefix="/api/auth/jwt", tags=["auth"])
    app.include_router(
        Routers.register_router,
        prefix="/api/auth",
        tags=["auth"],
    )
    app.include_router(
        Routers.reset_password_router,
        prefix="/api/auth",
        tags=["auth"],
    )
    app.include_router(
        Routers.verify_router,
        prefix="/api/auth",
        tags=["auth"],
    )
    app.include_router(
        Routers.users_router,
        prefix="/api/users",
        tags=["users"],
    )

    app.include_router(meal_router, prefix="/api/base")

    app.add_event_handler("startup", create_db_and_tables)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
