from uuid import UUID

from fastapi_users.schemas import BaseUser, BaseUserCreate, BaseUserUpdate


class UserRead(BaseUser[UUID]):
    username: str | None


class UserCreate(BaseUserCreate):
    username: str | None


class UserUpdate(BaseUserUpdate):
    username: str | None
