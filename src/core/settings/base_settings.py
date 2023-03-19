from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = "localhost"
    port: int = 8000

    class Config:
        env_file = ".env.example"
        env_file_encoding = "utf-8"


settings = Settings()
