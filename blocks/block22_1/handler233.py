from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

import getpath

path = getpath.pathreturn()
import time
from ..block23 import handler23
from ..block22 import handler22
from information_blocks.block233 import infohandler6
import createdb
def loads(message, bot, aaaa):
    if message.text == "Примеры прихожих":
        bot.delete_message(message.chat.id, aaaa)
        infohandler6.infoblock9_0(message, bot)
        
        return
    if message.text == "◀️ Назад":
        handler22.block4_11(message, bot)
        try:
            bot.delete_message(message.chat.id, aaaa)
        except Exception:
            pass
        return
    try:
        bot.delete_message(message.chat.id, aaaa)
    except Exception:
        pass
    createdb.exdb(message.text, 25, message.chat.id)
    handler23.block4_23(message, bot)
    

def block4_11(message: Message, bot):
    

    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(KeyboardButton("Примеры прихожих"))
    nazad = KeyboardButton("◀️ Назад")
    markup.add(nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожалуйста, в ответном сообщении укажите желаемую площадь зоны прихожей.</b>\n\n"
        "<i>Это удобно сделать в формате «вилки», например: от 15 до 25 м²</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
       
    
    


