from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class DBMeal(Base):
    __tablename__ = "meals"

    id: Mapped[int | None] = mapped_column(default=None, primary_key=True)
