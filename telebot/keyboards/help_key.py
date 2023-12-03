from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from telebot.lexicon.lexicon_ru import LEXICON_RU


# Функция создания инлайн кнопки "Назад" в главном меню
def create_help_keyboard() -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    kb_builder.row(
        InlineKeyboardButton(text=LEXICON_RU['email_button'], callback_data='email'),
        InlineKeyboardButton(text='Оплатить', callback_data='payment'),
        InlineKeyboardButton(text=LEXICON_RU['back'], callback_data='/start'),
        width=1)
    return kb_builder.as_markup()
