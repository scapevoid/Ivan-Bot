from telebot import TeleBot
from telebot.types import Message
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

import time

from getpath import pathreturn
from ..block4_2 import handler2
import createdb
path = pathreturn()


import time
from telebot.types import ReplyKeyboardRemove

def loads(message, bot, idaa):
    bot.delete_message(message.chat.id, idaa)
    createdb.exdb(message.text, 1, message.chat.id)
    handler2.block4_2(message, bot)

    

def block4_1(message: Message, bot):
    a = bot.send_message(
        message.chat.id,
        "🔵 Для оперативной связи:\n\n"
        "Пожалуйста, в ответном сообщении укажите <b>контактный номер для связи</b>.\n\n"
        "<i>Мы не передаем персонализированную информацию о своих клиентах третьим лицам.</i>",
        parse_mode="HTML"
    )
    
    bot.register_next_step_handler_by_chat_id(message.chat.id, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
    try:
        bot.delete_message(message.chat.id, message.id-1)
    except Exception:
        print("start error" + str(message.chat.id))
        pass
    
    


