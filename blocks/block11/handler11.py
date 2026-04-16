from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block12 import handler12
from ..block10 import handler10
import getpath

import time
path = getpath.pathreturn()
import createdb
import re


def loads(message, bot, aaaa):
    if message.text == "◀️ Назад":
        bot.delete_message(message.chat.id, aaaa)
        handler10.block4_10(message, bot)
        return
    # Проверяем, что введённое сообщение — это число в диапазоне 80-800, даже если есть слова или символы

    bot.delete_message(message.chat.id, aaaa)
    createdb.exdb(str(message.text.replace(',', '.')), 12, message.chat.id)
    handler12.block4_12(message, bot)

    

def block4_11(message: Message, bot):
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    nazad = KeyboardButton("◀️ Назад")
    markup.add(nazad)
    a = bot.send_message(message.chat.id, "<b>🔵Какой площади вы хотите построить дом?\n\nПожалуйста, напишите желаемую площадь.</b>\n\n"
                         "<i>Это удобно сделать в формате диапазона с разбегом 20 – 30 м2. Например: от 150 до 170 м2</i>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)


        
    
    


