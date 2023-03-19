from pydantic import BaseModel


class Meal(BaseModel):
    id: int | None = None
