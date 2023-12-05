import sqlite3
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from telebot.lexicon.lexicon_ru import LEXICON_RU
from telegram_bot_pagination import InlineKeyboardPaginator


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
def create_story_list_keyboard(arg) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    kb_builder = InlineKeyboardBuilder()
    # Наполняем клавиатуру кнопками-закладками
    kb_builder.row(*[InlineKeyboardButton(
        text=story_name,
        callback_data=story_name) for story_name in arg], width=1)
    kb_builder.row(*[InlineKeyboardButton(
        text=text,
        callback_data=comand)
        for text, comand in ((LEXICON_RU['backward'], 'backward'), (LEXICON_RU['forward'], 'forward'))], width=2)
    kb_builder.row(InlineKeyboardButton(
        text=LEXICON_RU['back'],
        callback_data='/start'))
    return kb_builder.as_markup()
