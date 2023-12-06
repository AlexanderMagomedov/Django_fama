from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from telebot.keyboards.keyboards import create_back_keyboard, create_story_list_keyboard
from telebot.keyboards.main_menu import create_menu_keyboard
from telebot.keyboards.help_key import create_help_keyboard
from telebot.lexicon.lexicon_ru import LEXICON_RU


router = Router()


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять ему приветственное сообщение показывать кнопки главного меню
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(LEXICON_RU[message.text], reply_markup=create_menu_keyboard())


# Этот хэндлер будет срабатывать на команду "/about_me"
# и отправлять пользователю сообщение с информацией о боте и кнопку "назад"
@router.message(Command(commands='about_me'))
async def process_about_me_command(message: Message):
    await message.answer(LEXICON_RU[message.text], reply_markup=create_back_keyboard('/start'))


# Этот хэндлер будет срабатывать на команду "/help"
# отправлять пользователю сообщение и клавиатуру меню "Поддержка"
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON_RU[message.text], reply_markup=create_help_keyboard())


# Этот хэндлер будет срабатывать на команду "/read"
# и отправлять пользователю список сказок в виде инлайн кнопок
@router.message(Command(commands='read'))
async def process_read_command(message: Message):
    start = 0
    await message.answer(LEXICON_RU[message.text], reply_markup=create_story_list_keyboard(start))
