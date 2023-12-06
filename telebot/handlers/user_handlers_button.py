from aiogram import F, Router
from aiogram.types import CallbackQuery

from telebot.books.book_list import page_list
from telebot.keyboards.keyboards import create_back_keyboard, create_story_list_keyboard
from telebot.keyboards.main_menu import create_menu_keyboard
from telebot.keyboards.help_key import create_help_keyboard
from telebot.lexicon.lexicon_ru import LEXICON_RU

router = Router()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "Назад"
@router.callback_query(F.data == '/start')
async def process_start(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/start'], reply_markup=create_menu_keyboard())
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "Обо мне" в главном меню показывает сообщение и кнопку "назад"
@router.callback_query(F.data == '/about_me')
async def process_about_me(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/about_me'], reply_markup=create_back_keyboard('/start'))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "Поддержка" в главном меню показывает сообщение и клавиатуру меню "Поддержка"
@router.callback_query(F.data == '/help')
async def process_help(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/help'], reply_markup=create_help_keyboard())
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "Читаем сказку" в главном меню
@router.callback_query(F.data == '/read')
async def process_read(callback: CallbackQuery):
    start = 0
    await callback.message.edit_text(
        text=LEXICON_RU['/read'],
        reply_markup=create_story_list_keyboard(start))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "Наша почта" в меню "Поддержка" выводить почту и кнопку "назад"
@router.callback_query(F.data == 'email')
async def process_email(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['email_send'], reply_markup=create_back_keyboard('/help'))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "Оплатить" в меню "Поддержка" выводить почту и кнопку "назад"
@router.callback_query(F.data == 'payment')
async def process_payment(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['payment'], reply_markup=create_back_keyboard('/help'))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# ">>" в меню выбора сказки
@router.callback_query((F.data).split()[0] == 'forward')
async def process_payment(callback: CallbackQuery):
    page = int(callback.data.split()[1]) + 1
    if page == len(page_list()):
        page = 0
    await callback.message.edit_text(
        text=LEXICON_RU['/read'],
        reply_markup=create_story_list_keyboard(page))
    await callback.answer()


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# "<<" в меню выбора сказки
@router.callback_query((F.data).split()[0] == 'backward')
async def process_payment(callback: CallbackQuery):
    page = int(callback.data.split()[1]) - 1
    if page < 0:
        page = len(page_list()) - 1
    await callback.message.edit_text(
        text=LEXICON_RU['/read'],
        reply_markup=create_story_list_keyboard(page))
    await callback.answer()


# # Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
# # в списке доступных сказок
# @router.callback_query(IsStory())
# async def process_cancel_press(callback: CallbackQuery):
#     await callback.message.edit_text(
#         text=getattr(books, book_name[callback.data]).book['Начало']['text'],
#         reply_markup=create_pagination_keyboard(getattr(books, book_name[callback.data]).book['Начало']['effect'],
#                                                 getattr(books, book_name[callback.data]).book['Начало']['button1'],
#                                                 getattr(books, book_name[callback.data]).book['Начало']['button2']))
#     await callback.answer()
