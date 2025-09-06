import asyncio
from aiogram import Bot, Dispatcher

async def main():
    bot = Bot(token="8314150363:AAEIFXX_fDDlB1L99VSGVPjMOi58klyBpOs")
    dp = Dispatcher()

    @dp.message()
    async def echo(msg):
        await msg.answer("Бот на связи. Скоро будет умным 🤖")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
