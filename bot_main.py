import asyncio
import logging
from aiogram.fsm.context import FSMContext
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.chat_action import ChatActionMiddleware
import parser
import keyboards
import yes_no_fun

class SearchState(StatesGroup):
    vibor = State()

answer_lek = ""
in_user = {}
logging.basicConfig(level=logging.INFO)
bot = Bot(token='6994195142:AAGS4WZuOaYNzc0sOEd4F_cPoWkS8rxqHqg')
dp = Dispatcher()
storage = MemoryStorage()
dp.message.middleware(ChatActionMiddleware())
check1 = 0
check2 = 1

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать! Вас приветствует сервис по поиску лекарств в аптеке uteka.ru")
    await message.answer("Чтобы я начал работу, подскажите, что вы ищите?")


@dp.message(StateFilter(None), F.text)
async def on_text_message(message: types.Message, state: FSMContext):
    await yes_no_fun.on_text_message(message, state)



@dp.message(lambda message: message.text == "Да", SearchState.vibor)
async def yes(message: types.Message, state: FSMContext):
    data = await state.get_data()
    current_index = data.get("index", 0)
    if current_index >= len(in_user):
        await message.answer("Больше вариантов нет.")
        return
    check1 = data.get("check1", 0)
    check2 = data.get("check2", 1)
    if check1 == 0:
        key = list(in_user.keys())[current_index]
        value = in_user[key]
        await message.answer(f"Вот например {key} по цене {value}")
        current_index += 1
    elif check1 == 1:
        if check2 == 1:
            current_index -= 2
            key = list(in_user.keys())[current_index]
            value = in_user[key]
            await message.answer(f"Вот например {key} по цене {value}")
            await state.update_data(check2=0)
        else:
            current_index -= 1
            key = list(in_user.keys())[current_index]
            value = in_user[key]
            await message.answer(f"Вот например {key} по цене {value}")

    await state.update_data(index=current_index)

    await ask_for_more(message)

async def ask_for_more(message: types.Message):
    await message.answer("Хотите увидеть ещё варианты?", reply_markup=keyboards.make_keyboard_ynb())

@dp.message(lambda message: message.text in {"Да", "Нет", "Назад"}, SearchState.vibor)
async def handle_yes_no(message: types.Message, state: FSMContext):
    await yes_no_fun.yes_no_back(message,state)

def filter(key, value):
    in_user[key] = value
    return in_user

def img(x):
    print(x)
async def main():
    await dp.start_polling(bot)
def start():
    return asyncio.run(main())