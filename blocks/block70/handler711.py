from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()

from ..block71 import handler71
from ..block69 import handler69
import createdb

def loads(message, bot, aa):
    if message.text == "◀️ Назад":
        handler69.block4_46(message, bot)
        bot.delete_message(message.chat.id, message.id)
        bot.delete_message(message.chat.id, aa) 
        return
    bot.delete_message(message.chat.id, message.id)
    bot.delete_message(message.chat.id, aa) 
    createdb.exdb(message.text, 80, message.chat.id)
    handler71.block4_40(message, bot)
    

def block4_40(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    nazad = KeyboardButton("◀️ Назад")
    markup.add(nazad)
    a = bot.send_message(message.chat.id, "<b>🔵 Пожалуйста, в ответном сообщении напишите о других известных вам особенностях участка, которые важно учитывать (ситуация на соседних участках, соседи, прочие особенности)</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
        
    
    


