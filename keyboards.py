from aiogram import types

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