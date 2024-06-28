from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from text import welcome_text

base_router = Router()


@base_router.message(Command('start'))
async def start(message: Message):
    await message.answer(text=welcome_text, parse_mode='HTML')
