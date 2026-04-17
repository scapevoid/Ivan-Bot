from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()

from ..block47_5 import handler47_5
from ..block46 import handler46
import time
import createdb

def loads(message, bot, aa):
    if message.text == "◀️ Назад":
        handler46.block4_46(message, bot)
        bot.delete_message(message.chat.id, aa)
        return

    bot.delete_message(message.chat.id, message.id)
    bot.delete_message(message.chat.id, aa) 
    createdb.exdb(message.text, 52, message.chat.id)
    handler47_5.block4_40(message, bot)
    

def block4_40(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    nazad = KeyboardButton("◀️ Назад")
    markup.add(nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожалуйста, в ответном сообщении укажите ориентировочную площадь кабинета.</b>\n\n"
        "<i>Это удобно сделать в формате «вилки», например: от 15 до 25 м2</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
    


