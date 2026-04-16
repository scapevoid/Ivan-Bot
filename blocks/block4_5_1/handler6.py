from telebot import TeleBot
from telebot.types import Message
import time

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery


from ..block4_5 import handler5
from ..block4_6 import handler4_6
import getpath
path = getpath.pathreturn()
import createdb

def loads(message, bot, aa):
    if message.text == "▶️ Пропустить":
        createdb.exdb("NULL", 6, message.chat.id)

        
        bot.delete_message(message.chat.id, aa)
        handler4_6.block4_5(message, bot)
        return
    if message.text == "◀️ Назад":
        handler5.block4_5(message, bot)
        bot.delete_message(message.chat.id, aa)
        return
    bot.delete_message(message.chat.id, aa)
    createdb.exdb(message.text, 6, message.chat.id)

    handler4_6.block4_5(message, bot)
    

def block4_6(message: Message, bot):
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    continue_btw = KeyboardButton("▶️ Пропустить")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(continue_btw, nazad)
    a = bot.send_message(
        message.chat.id,
        "<b>🔵Пожалуйста, в ответном сообщении опишите другие свои цели, что мы не упомянули</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda asd: loads(asd, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
    


        
    
    


