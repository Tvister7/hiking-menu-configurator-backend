from typing import Optional

from sqlmodel import Field, SQLModel


class Meal(SQLModel, table=True):
    # id: int | None = Field(default=None, primary_key=True)
    id: Optional[int] = Field(default=None, primary_key=True)
