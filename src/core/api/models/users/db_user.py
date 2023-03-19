from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.api.models.common import Base


class DBUser(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"
    username: Mapped[str | None] = mapped_column(String(255), default=None)
