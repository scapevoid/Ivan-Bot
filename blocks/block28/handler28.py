from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()
from ..block27.handler27 import cache as cache27
from ..block29 import handler29
from ..block27 import handler27
import time
import createdb
def loads(message, bot, aid):
    if message.text == "◀️ Назад":
        handler27.block4_27(message, bot)
        bot.delete_message(message.chat.id, aid)
        return

    bot.delete_message(message.chat.id, aid) 
    createdb.exdb(message.text, 32, message.chat.id)
    handler29.block4_28(message, bot)
    

def block4_28(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    nazad = KeyboardButton("◀️ Назад")
    markup.add(nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожалуйста, в ответном сообщении укажите желаемую площадь мастер-спальни.</b>\n\n"
        "<i>Это удобно сделать в формате «вилки», например: от 15 до 25 м2</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
    messages = cache27.get(message.chat.id, [])
    for msg in messages:
        bot.delete_message(message.chat.id, msg.message_id)
         
    
    


