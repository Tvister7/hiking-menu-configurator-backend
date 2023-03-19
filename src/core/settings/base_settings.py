from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    host: str = "localhost"
    port: int = 8000
    secret: SecretStr = SecretStr("my-big-secret")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
