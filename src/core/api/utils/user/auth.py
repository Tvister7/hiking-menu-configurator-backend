from typing import Annotated
from uuid import UUID

from fastapi import Depends, Request
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from loguru import logger

from core.api.models.users.db_user import DBUser
from core.api.utils.user.user_utils import get_user_db
from core.settings.base_settings import settings


class UserManager(UUIDIDMixin, BaseUserManager[DBUser, UUID]):  # type: ignore
    reset_password_token_secret = settings.secret.get_secret_value()
    verification_token_secret = settings.secret.get_secret_value()

    async def on_after_register(self, user: DBUser, request: Request | None = None):
        logger.info(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: DBUser, token: str, request: Request | None = None
    ):
        logger.info(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: DBUser, token: str, request: Request | None = None
    ):
        logger.info(
            f"Verification requested for user {user.id}. Verification token: {token}"
        )


async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.secret.get_secret_value(), lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[DBUser, UUID](  # type: ignore
    get_user_manager, [auth_backend]
)

current_active_user = fastapi_users.current_user(active=True)

UserAuth = Annotated[DBUser, Depends(current_active_user)]
