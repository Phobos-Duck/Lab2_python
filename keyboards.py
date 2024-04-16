from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import bot_main
import yes_no_fun

all_url = {}

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

def make_keyboard_url(key):
    kb = [[InlineKeyboardButton(text="Переход на сайт", callback_data=f"{all_url[key]}")]]
    inline_kb_full = types.InlineKeyboardMarkup(inline_keyboard=kb)
    return inline_kb_full


def url_forms(key, value):
    all_url[key] = value
    return all_url


