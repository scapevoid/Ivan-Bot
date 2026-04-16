from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery


import getpath
from ..block4_4 import handler4
from ..block4_2 import handler2
import createdb
import time

path = getpath.pathreturn()

import re

def loads(message, bot, asdasd):
    if message.text == "◀️ Назад":
        handler2.block4_2(message, bot)
        bot.delete_message(message.chat.id, asdasd)
        return
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, message.text):
        a = bot.send_message(message.chat.id, "Отправьте корректный email адрес")
        time.sleep(3)
        bot.delete_message(message.chat.id, asdasd)
        bot.delete_message(message.chat.id, a.id)
        block4_3(message, bot)
        return
    bot.delete_message(message.chat.id, asdasd)
    createdb.exdb(message.text, 3, message.chat.id)
    handler4.block4_4(message, bot)
    

def block4_3(message: Message, bot):
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    nazad = KeyboardButton("◀️ Назад")
    markup.add(nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 Для оперативной связи:\n\n"
        "Пожалуйста, в ответном сообщении укажите <b>вашу электронную почту для связи</b>.\n\n"
        "<i>Мы не передаем персонализированную информацию о своих клиентов третьим лицам.</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda asd: loads(asd, bot, a.id))

    bot.delete_message(message.chat.id, message.id)
    
    


