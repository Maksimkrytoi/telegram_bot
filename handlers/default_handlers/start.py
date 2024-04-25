from telebot.types import Message
from loader import bot
from keyboards.inline.main_kb import KB


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.reply_to(message, f"Привет, {message.from_user.full_name}!", reply_markup=KB)
