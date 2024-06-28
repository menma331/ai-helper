from aiogram import Bot, Dispatcher
from settings import settings
from openai import OpenAI


bot = Bot(token=settings.bot_token)
disp = Dispatcher()
client = OpenAI(
    api_key=settings.openai_token
)

