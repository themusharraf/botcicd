from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import CommandStart
import asyncio

BOT_TOKEN = "7569570451:AAFo3LPGklMyWIc5yT7AhNawJKB6pZqsB9Y" # bot new add gits

bot = Bot(token=BOT_TOKEN) #tt
dp = Dispatcher()


@dp.message(CommandStart())
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
