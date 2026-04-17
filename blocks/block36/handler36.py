from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()

from ..block37 import handler37
from ..block35 import handler35
import time
import createdb

def loads(message, bot, aaaa):
    if message.text == "▶️ Пропустить":
        createdb.exdb("NULL", 40, message.chat.id)
        handler37.block4_37(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    if message.text == "◀️ Назад":
        handler35.block4_32(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    bot.delete_message(message.chat.id, aaaa)
    createdb.exdb(message.text, 40, message.chat.id)
    handler37.block4_37(message, bot)
    

def block4_36(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    continue_btw = KeyboardButton("▶️ Пропустить")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(continue_btw, nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожалуйста, в ответном сообщении расскажите нам о своих пожеланиях к гостевой зоне.</b>\n\n"
        "<i>Если дополнительных идей пока нет или вы хотели бы обсудить этот пункт на личной встрече – пожалуйста, пропустите этот вопрос.</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
        
    
    


