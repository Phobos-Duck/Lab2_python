from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton


dp = Dispatcher()
def make_keyboard_yn():
    kb = [
        [
            types.KeyboardButton(text="Да"),
            types.KeyboardButton(text="Нет")
        ],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Выберите действие")


def make_keyboard_ynb():
    kb = [
        [
            types.KeyboardButton(text="Да"),
            types.KeyboardButton(text="Нет"),
            types.KeyboardButton(text="Назад"),
            types.KeyboardButton(text="Я определился на текущем")

        ],
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder="Выберите действие")

def make_keyboard_url(url):
    kb = [[InlineKeyboardButton(text="Переход на сайт", url=url)]]
    inline_kb_full = types.InlineKeyboardMarkup(inline_keyboard=kb)
    return inline_kb_full





