from telebot import types

KB = types.InlineKeyboardMarkup(row_width=3)
btn1 = types.InlineKeyboardButton(text='1',callback_data="1")
btn2 = types.InlineKeyboardButton(text='2',callback_data="2")
btn3 = types.InlineKeyboardButton(text='3',callback_data="3")

KB.add(btn1,btn2,btn3)