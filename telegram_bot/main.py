from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from api import create_user


async def get_domains_info(message):
    await message.answer("Nima gap tuzumisan? Karochi mana\
        sanga polniy data")


def get_buttons(buttons, lang=None, n=2):
    rkm = types.ReplyKeyboardMarkup(True, row_width=n, resize_keyboard=True)
    if lang is None:
        rkm.add(*(types.KeyboardButton(btn) for btn in buttons))
    else:
        rkm.add(*(types.KeyboardButton(btn[lang]) for btn in buttons))
    return rkm

UZ = 'UZ'
RU = 'RU'


DOMAINS = 'Domains'
LIST_LANG = [UZ, RU]
MENU_BUTTONS = [DOMAINS]

class UserState(StatesGroup):

    language = State()
    menu = State()

BOT_TOKEN = "1878898481:AAHBhPKTn63PV5fCAGN4O8Ubuu7lLiJse7Q"

bot = Bot(BOT_TOKEN, parse_mode=None)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands='start')
async def on_start(message: types.Message):
    print("Working...")
    print("In on start handler")
    await message.answer("Tillardan birini tanlang: ", reply_markup=get_buttons(LIST_LANG))

    await UserState.language.set()

@dp.message_handler(state=UserState.language)
async def on_language(message: types.Message, state: FSMContext):
    print("In on language handler")
    if message.text == UZ:
        print("Uzbek language chosen")
    if message.text == RU:
        print("Russian language chosen")

    await state.update_data(
        {
            "language": message.text
        }
    )


    data = await state.get_data()
    print("Creating user")
    await create_user(message.from_user.id, message.chat.id, lang=data['language'])
    
    print("User created")
    # every handler need get user for checking is authorized or no
    # here is need to write request code for creating new user

    await message.answer("Foydalanuvchi tili qabul qilindi!", reply_markup=get_buttons(MENU_BUTTONS))
    await UserState.next()



@dp.message_handler(state=UserState.menu)
async def on_menu(message: types.Message, state: FSMContext):
    await message.answer("Asosiy menu")
    if message.text == DOMAINS:
        await get_domains_info(message)
    await state.finish()

if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)

