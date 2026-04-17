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
from ..block53_3 import handler54_3
from ..block53_1 import handler54_1
import createdb
def loads(message, bot, aa):
    if message.text == "▶️ Пропустить":
        createdb.exdb("NULL", 61, message.chat.id)
        handler54_3.block4_53(message, bot)
        bot.delete_message(message.chat.id, aa)
        return
    if message.text == "◀️ Назад":
        handler54_1.block4_53(message, bot)
        bot.delete_message(message.chat.id, aa)
        return
    bot.delete_message(message.chat.id, aa)
    createdb.exdb(message.text, 61, message.chat.id)
    handler54_3.block4_53(message, bot)


def block4_53(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    continue_btw = KeyboardButton("▶️ Пропустить")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(KeyboardButton("2.6 - 2.7 м"))
    markup.add(KeyboardButton("2.7 - 2.9 м"))
    markup.add(KeyboardButton("2.9 - 3.1 м"))
    markup.add(KeyboardButton("3.1 - 3.5 м"))
    markup.add(KeyboardButton("3.6 - 4.0 м"))
    markup.add(continue_btw, nazad)
    a = bot.send_message(message.chat.id, "<b>🔵 Укажите желаемую высоту потолков комнат первого этажа</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)   
