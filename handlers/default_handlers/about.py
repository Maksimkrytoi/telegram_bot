from telebot.types import Message

from loader import bot



@bot.message_handler(commands=["about"])
def about(message: Message):
    bot.reply_to(
        message, "Нат данным ботом усердно работает Лимаренко Максим-Великий программист!"
    )
