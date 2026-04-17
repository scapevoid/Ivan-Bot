from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()
import time
from ..block39 import handler39
from ..block37 import handler37
import createdb

def loads(message, bot, aaaa):
    if message.text == "▶️ Пропустить":
        createdb.exdb("NULL", 42, message.chat.id)
        handler39.block4_39(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    if message.text == "◀️ Назад":
        handler37.block4_37(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    if not message.text.isdigit():
        a = bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение")
        time.sleep(3)
        bot.delete_message(message.chat.id, a.id)
        bot.delete_message(message.chat.id, aaaa) 
        block4_38(message, bot)
        return
    bot.delete_message(message.chat.id, aaaa) 
    createdb.exdb(message.text, 42, message.chat.id)
    handler39.block4_39(message, bot)
    

def block4_38(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    continue_btw = KeyboardButton("▶️ Пропустить")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(continue_btw, nazad)
    a = bot.send_message(message.chat.id, "<b>🔵 Пожалуйста в ответном сообщении укажите ориентировочную площадь санузла №1 (санузел в мастер-спальне)</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
    
    


