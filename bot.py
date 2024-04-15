import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import parser


answer_lek = ""
in_user = {}
logging.basicConfig(level=logging.INFO)
bot = Bot(token='6994195142:AAGS4WZuOaYNzc0sOEd4F_cPoWkS8rxqHqg')
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать! Вас приветствует сервис по поиску лекарств в аптеке uteka.ru")
    await message.answer("Чтобы я начал работу, подскажите, что вы ищите?")

@dp.message(F.text)
async def on_text_message(message: types.Message):
    answer_lek = message.text
    await message.reply(f"Понял! Попробую найти {answer_lek}")
    parser.parse(answer_lek)
    for key, value in in_user.items():
        await message.answer(f"Вот например{key} по цене {value}")
async def main():
    await dp.start_polling(bot)

def filtered(**filtered):
    for key, value in filtered.items():
        in_user[key] = value
def start():
    asyncio.run(main())