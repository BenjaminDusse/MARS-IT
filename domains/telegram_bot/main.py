import logging
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from domains.telegram_bot import db_utils, const, utils
from domains.models import UZ, RU

from domains.telegram_bot.states import UserState

BOT_TOKEN = "1878898481:AAHBhPKTn63PV5fCAGN4O8Ubuu7lLiJse7Q"
logging.basicConfig(level=logging.DEBUG)

bot = Bot(BOT_TOKEN, parse_mode=None)
dp = Dispatcher(bot, storage=MemoryStorage())


# class UserState:
    # start = 0
    # language = 1
    # contact = 2
    # verification = 3
    # main_menu = 4
    # personal = 5
    # personal_deposit_source = 6
    # personal_deposit_currency = 7
    # personal_deposit_bank = 8
    # personal_deposit_mobile = 9
    # personal_credit_type = 10
    # personal_credit = 11
    # personal_card_currency = 12
    # personal_card = 13
    # corporate = 15
    # entrepreneur = 20
    # regions = 25
    # branches = 30
    # settings = 35
    # change_language = 36
    # contact_us = 40
    # write_consultant = 41


@dp.message_handler(commands=['start'])
async def start(message):
    send_welcome(message)
    await check_user(message.chat.id, message.from_user.id)


print("Working")
# Bot Handlers

# register
@dp.message_handler(state=UserState.language)
async def language_handler(message: types.Message, state: FSMContext):
    await ask_language(message.chat.id)
    await state.finish()
    # user_id = message.from_user.id
    # user = await db_utils.get_user(user_id)
    # if not user:
    #     await send_error(message.chat.id)
    # elif message.text == const.UZBEK:
    #     await db_utils.set_user_lang(user, UZ)
    #     await ask_contact(message.chat.id, user.lang)
    # elif message.text == const.RUSSIAN:
    #     await db_utils.set_user_lang(user, RU)
    #     await ask_contact(message.chat.id, user.lang)
    # else:
    #     await send_error_choice(message.chat.id, user.lang)


# @dp.message_handler(content_types=["contact"])
# async def phone_number_handler(message):
#     user_id = message.from_user.id
#     user = await db_utils.get_user(user_id)
#     if bot.get_state(message.chat.id) != UserState.contact:
#         await send_error(message.chat.id)
#         return
#     phone_number = utils.get_phone_number(message.contact)
#     if not phone_number:
#         await send_error(message.chat.id)
#         return
#     await db_utils.set_phone_number(user, phone_number)
#     await send_notify(message.chat.id, phone_number, user.lang)


# @dp.message_handler(state=UserState.verification)
# async def verification_handler(message):
#     user_id = message.from_user.id
#     user = await db_utils.get_user(user_id)
#     if not user:
#         await send_error(message.chat.id)
#         return
#     elif user.code != message.text:
#         await send_wrong_code(message.chat.id, user.lang)
#         return
#     await db_utils.set_user_verified(user)
#     await send_main_menu(user)


# # main menu
# @dp.message_handler(state=UserState.main_menu)
# async def main_menu_handler(message):
#     await bot.send_message(message.chat.id)

# # Methods

def check_user(chat_id, tg_user_id):
    user = db_utils.get_user(chat_id)
    if not user:
        db_utils.create_user(chat_id, tg_user_id)
        send_welcome(chat_id)
        ask_language(chat_id)
    elif not user.lang:
        ask_language(chat_id)
    elif not user.phone_number:
        ask_contact(chat_id, user.lang)
    elif not user.is_verified:
        send_notify(chat_id, user.phone_number, user.lang)
    elif user.is_verified:
        send_main_menu(user)
    else:
        send_error(chat_id)


# Send message

# start


def send_welcome(message):
    bot.send_message(message, const.WELCOME_MESSAGE, reply_markup=utils.get_buttons(const.LIST_LANG))

# register

def ask_language(chat_id):
    bot.send_message(chat_id, const.ASK_LANGUAGE,
                     reply_markup=utils.get_buttons(const.LIST_LANG))
    UserState.language.set()
    # bot.set_state(FsmContext(state=UserState.language))


def ask_contact(chat_id, lang):
    bot.send_message(
        chat_id, const.ASK_PHONE_NUMBER[lang], reply_markup=utils.get_phone_number_button(lang))    
    bot.set_state(FsmContext(state=UserState.contact))


def send_notify(chat_id, phone_number, lang):
    bot.send_message(chat_id, const.SENT_NOTIFY[lang].format(
        phone_number=phone_number), reply_markup=utils.get_remove_keyboard())
    bot.set_state(FsmContext(state=UserState.verification))

def send_wrong_code(chat_id, lang):
    bot.send_message(chat_id, const.WRONG_CODE[lang])


def send_phone_number_not_found(chat_id, lang):
    bot.send_message(chat_id, const.WRONG_PHONE_NUMBER[lang])


# main menu
def send_main_menu(user):
    bot.send_message(
        user.chat_id, const.MAIN_MENU[user.lang], reply_markup=utils.get_main_menu_keyboard(user.lang))
    bot.set_state(FsmContext(state=UserState.main_menu))
    

# etc
def send_currency(chat_id, lang):
    bot.send_message(chat_id, utils.get_currency(lang), parse_mode="html")


def send_error(chat_id):
    bot.send_message(chat_id, const.ERROR)
    bot.set_state(FsmContext(state=UserState.start))
    

def send_error_choice(chat_id, lang):
    bot.send_message(chat_id, const.ERROR_CHOICE[lang])


def send_no_content(chat_id, lang):
    bot.send_message(chat_id, const.NO_CONTENT[lang])

