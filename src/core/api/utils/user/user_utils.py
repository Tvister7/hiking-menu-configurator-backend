from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

from core.api.models.users.db_user import DBUser
from core.external.postgres import AnnotatedSession


async def get_user_db(session: AnnotatedSession):
    yield SQLAlchemyUserDatabase(session, DBUser)  # type: ignore
