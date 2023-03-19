from sqlalchemy.orm import Mapped, mapped_column

from core.api.models.common import Base


class DBMeal(Base):
    __tablename__ = "meals"

    id: Mapped[int | None] = mapped_column(default=None, primary_key=True)
