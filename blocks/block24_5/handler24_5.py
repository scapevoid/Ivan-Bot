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
from ..block25 import handler25 
from ..block24 import handler24
from information_blocks.block245 import infohandler6
import createdb
def loads(message, bot, aaaa):
    if message.text == "Примеры кухонь":
        infohandler6.infoblock9_0(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    if message.text == "◀️ Назад":
        handler24.block4_24(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return

    bot.delete_message(message.chat.id, aaaa) 
    createdb.exdb(message.text, 28, message.chat.id)
    handler25.block4_25(message, bot)
    

def block4_24(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    asda = KeyboardButton("Примеры кухонь")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(asda, nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожалуйста, в ответном сообщении укажите примерную желаемую площадь зоны кухни.</b>\n\n"
        "<i>Это удобно сделать в формате «вилки», например: от 15 до 25 м²</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)

    


