from pydantic import BaseSettings


class Settings(BaseSettings):
    user: str | None = None
    password: str | None = None
    host: str | None = None
    port: int = 8000
    initial_db: str | None = None

    url: str | None = None

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "postgres_"

    def get_pg_url(self) -> str:
        if self.url:
            return self.url

        url = f"postgresql://{self.user}:" f"{self.password}@{self.host}:{self.port}/"

        if self.initial_db:
            url += f"{self.initial_db}"

        self.url = url

        return url


settings = Settings()
