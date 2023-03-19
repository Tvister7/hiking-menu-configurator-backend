from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class DBUser(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255), default=None)
    fullname: Mapped[str | None] = mapped_column(String(255), default=None)
    hashed_password: Mapped[str] = mapped_column(String(2047))
