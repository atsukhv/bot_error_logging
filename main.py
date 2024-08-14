from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from logg_mdw.middleware import ErrorLoggingMiddleware


async def main():
    await async_main()
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.update.middleware(ErrorLoggingMiddleware())
    await dp.start_polling(bot)


if __name__ == '__main__':
