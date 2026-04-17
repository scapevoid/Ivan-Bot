from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()

from information_blocks.block14_3 import infohandler14_3
from ..block73.handler73 import cache as cache33
from ..block71 import handler71
import createdb


def loads(message, bot, aa):
    if message.text == "◀️ Назад":
        handler71.block4_40(message, bot)
        bot.delete_message(message.chat.id, message.id)
        bot.delete_message(message.chat.id, aa) 
        return
    bot.delete_message(message.chat.id, message.id)
    bot.delete_message(message.chat.id, aa) 
    createdb.exdb(message.text, 82, message.chat.id)
    infohandler14_3.infoblock10_5(message, bot)
    

def block4_40(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    nazad = KeyboardButton("◀️ Назад")
    markup.add(nazad)
    a = bot.send_message(message.chat.id, "<b>🔵 Пожалуйста, в ответном сообщении напишите желаемую дату новоселья</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
    messages = cache33.get(message.chat.id, [])
    for msg in messages:
        bot.delete_message(message.chat.id, msg.message_id)
        
    
    


