from aiogram.fsm.context import FSMContext
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.state import StatesGroup, State
import bot_main
import parser
import keyboards
import parser_img
import parser_url
dp = Dispatcher()
class SearchState(StatesGroup):
    vibor = State()

all_url = []
bot = Bot(token='6994195142:AAGS4WZuOaYNzc0sOEd4F_cPoWkS8rxqHqg')

async def on_text_message(message: types.Message, state: FSMContext):
    answer_lek = message.text
    p_n = parser.parse(answer_lek)
    p_u = parser_url.parse(answer_lek)
    p_i = parser_img.parse(answer_lek)
    await message.reply(f"Понял! Попробую найти {answer_lek}")
    if(p_n == False):
        all_url.clear()
        bot_main.clear_list()
        await message.answer("Извините, я ничего не смог найти по вашему запросу. Попробуйте снова ввести симптом или название препарата.")
    else:
        await message.reply("Я нашел несколько вариантов. Показать?", reply_markup=keyboards.make_keyboard_yn())
        await state.set_state(SearchState.vibor)

async def yes_no_back(message: types.Message, state: FSMContext):
    data = await state.get_data()
    current_index = data.get("index", 0)
    if message.text == "Да":
        await on_text_message(message, state)
        await state.update_data(check1=0)
        await state.update_data(check2=1)
    elif message.text == "Нет":
        await message.answer("Вы не нашли то что искали? Извините,что не смог ничем помочь:(", reply_markup=types.ReplyKeyboardRemove())
        all_url.clear()
        bot_main.clear_list()
        await state.clear()
    elif message.text == "Назад":
        if current_index > 0:
            await state.update_data(check1=1)
            await bot_main.yes(message, state)
        else:
            await state.update_data(check2=0)
            await state.update_data(check1=0)
            await message.answer("Нельзя вернуться назад.")
    elif message.text == "Я определился на текущем":
        data = await state.get_data()
        current_index = data.get("index", 0)
        url = all_url[current_index]
        await message.answer("Я рад, что смог вам помочь! Вот ссылка для перехода на сайт.", reply_markup=keyboards.make_keyboard_url(url))
        await message.answer("Если хотите снова найти что-то, напишите название препарата или симптом", reply_markup=types.ReplyKeyboardRemove())
        bot_main.clear_list()
        all_url.clear()
        await state.clear()

def url_forms(value):
    all_url.append(value)