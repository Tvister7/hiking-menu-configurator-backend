from fastapi.routing import APIRouter

from core.api.models.users.user import UserCreate, UserRead, UserUpdate
from core.api.utils.user.auth import auth_backend, fastapi_users


class Routers:
    auth_router: APIRouter = fastapi_users.get_auth_router(auth_backend)
    register_router: APIRouter = fastapi_users.get_register_router(UserRead, UserCreate)
    reset_password_router: APIRouter = fastapi_users.get_reset_password_router()
    verify_router: APIRouter = fastapi_users.get_verify_router(UserRead)
    users_router: APIRouter = fastapi_users.get_users_router(UserRead, UserUpdate)
