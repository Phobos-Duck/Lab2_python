import asyncio
import logging
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder
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
async def on_text_message(message: types.Message, state:FSMContext):
    answer_lek = message.text
    await message.reply(f"Понял! Попробую найти {answer_lek}")
    parser.parse(answer_lek)
    await message.reply("Я нашел несколько вариантов. Показать?", reply_markup=make_keyboard())

def make_keyboard():
    kb = ReplyKeyboardBuilder()
    kb.button(text="Да", callback_data=Command.new(function='yes'))
    kb.button(text="Нет", callback_data=Command.new(function='no'))
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
@dp.callback_query_handler(Command.filter(function='yes'))
async def yes(query: types.CallbackQuery, callback_data: dict):
    await bot.send_message("Хорошо! Дайте мне секунду...")
    for key, value in in_user.items():
        for i in len(in_user):
            await bot.send_message(f"Вот например{in_user[i][key]} по цене {in_user[i][value]}")

async def go(message: types.Message, state: FSMContext):
    for key, value in in_user.items():
        for i in len(in_user):
            await message.answer(f"Вот например{in_user[i][key]} по цене {in_user[i][value]}")
async def main():
    await dp.start_polling(bot)

def filter(key, value):
    in_user[key] = value
def start():

    asyncio.run(main())