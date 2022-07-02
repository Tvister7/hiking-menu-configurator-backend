from pydantic import BaseSettings


class Settings(BaseSettings):

    host: str
    port: int
    country: str = "ru"

    postgres_url: str

    class Config:
        env_file = ".env.example"
        env_file_encoding = "utf-8"


settings = Settings()  # type: ignore
