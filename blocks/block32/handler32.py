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

from ..block33 import handler33
from ..block31 import handler31
import createdb
def loads(message, bot, aaaa):
    if message.text == "◀️ Назад":
        handler31.block4_31(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return

    bot.delete_message(message.chat.id, aaaa) 
    createdb.exdb(message.text, 36, message.chat.id)
    handler33.block4_32(message, bot)
    

def block4_32(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    nazad = KeyboardButton("◀️ Назад")
    markup.add(nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожалуйста, в ответном сообщении укажите желаемую среднюю площадь детской спальни.</b>\n\n"
        "<i>Это удобно сделать в формате «вилки», например: от 15 до 25 м2</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)   
    
    


