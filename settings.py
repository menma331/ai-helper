from pydantic import (
    Field,
)

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Модель настроек.

    Аттрибуты:
        * `bot_token`: Токен телеграм бота.
        * `openai_token`: Токен OpenAI.
    """
    bot_token: str = Field(alias='TELEGRAM_BOT_TOKEN')
    openai_token: str = Field(alias='OPEN_AI_TOKEN')
    proxy: str = Field(alias='PROXY')

    class Config:
        env_file = '.env'


settings = Settings()
