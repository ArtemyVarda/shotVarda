import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from heandlers import Main as heand



async def main():
    print('bot start')

    bot = Bot(TOKEN, parse_mode='HTML')
    dp = Dispatcher()
    dp.include_routers(heand.roater)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('bot dead')