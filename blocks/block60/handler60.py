from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()

from ..block61 import handler61
from ..block59 import handler59
import time
import createdb
def loads(message, bot, aa):
    if message.text == "◀️ Назад":
        handler59.block4_40(message, bot)
        bot.delete_message(message.chat.id, aa)
        return
    if not message.text.isdigit():
        a = bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение")
        time.sleep(3)
        bot.delete_message(message.chat.id, a.id)
        bot.delete_message(message.chat.id, aa) 

        block4_40(message, bot)
    bot.delete_message(message.chat.id, aa) 
    createdb.exdb(message.text, 70, message.chat.id)
    handler61.block4_61(message, bot)
    

def block4_40(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    nazad = KeyboardButton("◀️ Назад")
    markup.add(nazad)
    a = bot.send_message(message.chat.id, "<b>🔵 Пожалуйста, в ответном сообщении укажите площадь участка в сотках</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)   
    
    


