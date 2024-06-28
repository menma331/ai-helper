import asyncio
import logging

import openai

from handlers.base import base_router
from handlers.voice_assistent import assistant_router
from loader import disp, bot
from settings import settings


async def run_bot():
    openai.api_key = settings.openai_token
    logging.basicConfig(level=logging.INFO)
    disp.include_router(base_router)
    disp.include_router(assistant_router)
    await disp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(run_bot())
