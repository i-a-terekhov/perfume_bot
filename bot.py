import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from hidden.tokenfile import TOKEN
from handlers.echo import service_router, regular_router

bot_unit = Bot(TOKEN)


async def main(bot):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher(
        storage=MemoryStorage(),
        maintenance_mode=False  # режим обслуживания бота (True - заглушка, False - начальные приветственные сообщения)
    )

    dp.include_routers(
        service_router,
        regular_router,
        )

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main(bot=bot_unit))
