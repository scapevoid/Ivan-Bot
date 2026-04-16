from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

import getpath

path = getpath.pathreturn()

from ..block22_1 import handler233
from ..block21 import handler21
import createdb

def loads(message, bot, aaaa):
    if message.text == "▶️ Пропустить":
        createdb.exdb("NULL", 24, message.chat.id)
        handler233.block4_11(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    if message.text == "◀️ Назад":
        handler21.block4_21(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    bot.delete_message(message.chat.id, aaaa)
    createdb.exdb(message.text, 24, message.chat.id)
    handler233.block4_11(message, bot)
    

def block4_11(message: Message, bot):
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    continue_btw = KeyboardButton("▶️ Пропустить")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(continue_btw, nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожелания к входной зоне</b>\n\n"
        "<b>Пожалуйста, в ответном сообщении расскажите нам о своих пожеланиях к входной зоне.</b>\n\n"
        "<i>Если дополнительных идей пока нет или вы хотели бы обсудить этот пункт на личной встрече с нашей командой – просто пропустите этот вопрос.</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
        
    
    


