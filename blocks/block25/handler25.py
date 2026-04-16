from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()

from ..block26 import handler26 
from ..block24_5 import handler24_5
import time
import createdb
from information_blocks.block25 import infohandler6
from information_blocks.block25.infohandler6 import cache
def loads(message, bot, aaaa):
    if message.text == "Примеры терасс":
        infohandler6.infoblock9_0(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    if message.text == "◀️ Назад":
        bot.delete_message(message.chat.id, aaaa)
        handler24_5.block4_24(message, bot)
        return
    bot.delete_message(message.chat.id, aaaa) 
    createdb.exdb(message.text, 29, message.chat.id)
    handler26.block4_26(message, bot)
    

def block4_25(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    nazad = KeyboardButton("◀️ Назад")
    asda = KeyboardButton("Примеры терасс")
    markup.add(asda, nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожалуйста, в ответном сообщении укажите желаемую площадь террасы.</b>\n\n"
        "<i>Это удобно сделать в формате «вилки», например: от 15 до 25 м²</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
    
    


