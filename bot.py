import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command


answer_lek = ""
logging.basicConfig(level=logging.INFO)
bot = Bot(token='6994195142:AAGS4WZuOaYNzc0sOEd4F_cPoWkS8rxqHqg')
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать! Вас приветствует сервис по поиску лекарств в аптеке uteka.ru")
    await message.answer("Чтобы я начал работу, подскажите, что вы ищите?")

@dp.message(content_types=types.ContentType.TEXT)
async def on_text_message(message: types.Message):
    await message.reply("Понял! Попробую найти...")
async def main():
    await dp.start_polling(bot)
def start():
    asyncio.run(main())