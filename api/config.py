from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def database_url(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    BOT_TOKENS: str

    @property
    def bot_tokens(self):
        return self.BOT_TOKENS.split(",")

    class Config:
        env_file = ".env"


settings = Settings()
