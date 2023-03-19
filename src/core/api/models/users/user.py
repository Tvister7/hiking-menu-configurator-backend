from pydantic import BaseModel


class User(BaseModel):
    email: str
    username: str | None = None
    fullname: str | None = None


class UserInDB(User):
    id: int | None = None
    hashed_password: str
