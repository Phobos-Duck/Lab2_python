import asyncio
import logging
from aiogram.fsm.context import FSMContext
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.state import StatesGroup, State
from aiogram.utils.chat_action import ChatActionMiddleware
import parser


answer_lek = ""
in_user = {}
logging.basicConfig(level=logging.INFO)
bot = Bot(token='6994195142:AAGS4WZuOaYNzc0sOEd4F_cPoWkS8rxqHqg')
dp = Dispatcher()
storage = MemoryStorage()
dp.message.middleware(ChatActionMiddleware())
check1 = 0
chek2 = 0
class SearchState(StatesGroup):
    vibor = State()
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать! Вас приветствует сервис по поиску лекарств в аптеке uteka.ru")
    await message.answer("Чтобы я начал работу, подскажите, что вы ищите?")


@dp.message(StateFilter(None), F.text)
async def on_text_message(message: types.Message, state: FSMContext):
    answer_lek = message.text
    parser.parse(answer_lek)
    await message.reply(f"Понял! Попробую найти {answer_lek}")
    answer_lek = message.text
    await message.reply("Я нашел несколько вариантов. Показать?", reply_markup=make_keyboard_yn())
    await state.set_state(SearchState.vibor)


@dp.message(lambda message: message.text == "Да", SearchState.vibor)
async def yes(message: types.Message, state: FSMContext):
    data = await state.get_data()
    current_index = data.get("index", 0)
    if current_index >= len(in_user):
        await message.answer("Больше вариантов нет.")
        return

    check = data.get("check", 0)

    if check == 0:
        key = list(in_user.keys())[current_index]
        value = in_user[key]
        await message.answer(f"Вот например {key} по цене {value}")
        current_index += 1
    elif check == 1:
        current_index -= 2
        key = list(in_user.keys())[current_index]
        value = in_user[key]
        await message.answer(f"Вот например {key} по цене {value}")

    await state.update_data(index=current_index)

    await ask_for_more(message)

async def ask_for_more(message: types.Message):
    await message.answer("Хотите увидеть ещё варианты?", reply_markup=make_keyboard_ynb())

@dp.message(lambda message: message.text in {"Да", "Нет", "Назад"}, SearchState.vibor)
async def handle_yes_no(message: types.Message, state: FSMContext):
    data = await state.get_data()
    current_index = data.get("index", 0)
    if message.text == "Да":
        await on_text_message(message, state)
        await state.update_data(check=0)  # Устанавливаем check в 0
    elif message.text == "Нет":
        await message.answer("Спасибо за использование нашего сервиса!")
    elif message.text == "Назад":
        if current_index > 0:
            await state.update_data(check=1)  # Устанавливаем check в 1
            await yes(message, state)
        else:
            await message.answer("Нельзя вернуться назад.")

def make_keyboard_yn():
    kb = [
        [
            types.KeyboardButton(text="Да", callback_data='yes'),
            types.KeyboardButton(text="Нет", callback_data='no')
        ],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Выберите действие")


def make_keyboard_ynb():
    kb = [
        [
            types.KeyboardButton(text="Да", callback_data='yes'),
            types.KeyboardButton(text="Нет", callback_data='no'),
            types.KeyboardButton(text="Назад", callback_data='back')

        ],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Выберите действие")

def filter(key, value):
    in_user[key] = value
    return in_user

async def main():
    await dp.start_polling(bot)
def start():
    asyncio.run(main())