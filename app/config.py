"""Конфигурация приложения"""
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8",
    )

    debug: bool = False

    redis_url: str = "redis://127.0.0.1:6379/0"
    project_name: str = "newsbot"

    telegram_api_id: int = 0
    telegram_api_hash: str = ""
    telegram_phone: str = ""
    # telegram_bot_token: str = ""
    # telegram_channel_id: str = ""

    news_keywords: str = "python,fastapi,ai,django,нейросети,airogram"

    @property
    def keywords_list(self) -> list[str]:
        raw_value = self.news_keywords
        parts = [part.strip() for part in raw_value.split(",") if part.strip()]
        return parts


settings = Settings()