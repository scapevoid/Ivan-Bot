from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()

from ..block41_3 import handler41_3
from ..block39 import handler39
import time
import createdb
def loads(message, bot, aaaa):
    if message.text == "▶️ Пропустить":
        createdb.exdb("NULL", 44, message.chat.id)
        handler41_3.block4_34(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return

    bot.delete_message(message.chat.id, aaaa) 
    createdb.exdb(message.text, 44, message.chat.id)
    handler41_3.block4_34(message, bot)
    

def block4_40(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    continue_btw = KeyboardButton("▶️ Пропустить")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(continue_btw, nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожалуйста, в ответном сообщении укажите ориентировочную площадь санузла №2</b>\n\n"
        "<i>Это удобно сделать в формате «вилки», например: от 15 до 25 м2</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)  
    
    


