from aiogram import Router, F
from aiogram.types import Message

from ai_services import convert_voice_to_text
from loader import bot
from settings import settings

assistant_router = Router()


@assistant_router.message(F.voice)
async def handle_voice_message(message: Message):
    voice = message.voice
    file_info = await bot.get_file(voice.file_id)
    file_path = file_info.file_path
    file_url = f"https://api.telegram.org/file/bot{settings.bot_token}/{file_path}"
    converted_text = convert_voice_to_text(file_url)
    await message.answer(text=converted_text, parse_mode='HTML')
