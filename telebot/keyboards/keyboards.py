from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from telebot.lexicon.book_name import book_name

from telebot.lexicon.lexicon_ru import LEXICON_RU


# Функция создания инлайн кнопки "Назад" в главном меню
def create_back_keyboard(arg) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками в порядке возрастания
    kb_builder.row(InlineKeyboardButton(
        text=LEXICON_RU['back'],
        callback_data=arg))
    return kb_builder.as_markup()


# Функция создания инлайн кнопкок со списком сказок
def create_story_list_keyboard() -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками
    kb_builder.row(*[InlineKeyboardButton(
        text=story_name,
        callback_data=story_name) for story_name in book_name.keys()], width=1)
    kb_builder.row(InlineKeyboardButton(
        text=LEXICON_RU['back'],
        callback_data='/start'))
    return kb_builder.as_markup()
