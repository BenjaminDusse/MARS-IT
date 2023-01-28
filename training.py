import logging
from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = "1878898481:AAHBhPKTn63PV5fCAGN4O8Ubuu7lLiJse7Q"

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def on_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text="Raqamni yuborish", request_contact=True),
        types.KeyboardButton(text="Geolokatsiyani yuborish", request_location=True),
        types.KeyboardButton(text="Yangi so'rovnoma yoki quiz yaratish", request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ))
    )

    await message.answer(
        text=f"Salom {message.from_user.full_name}!",
        reply_markup=keyboard
    )

if __name__=="__main__":
    executor.start_polling(dp)
