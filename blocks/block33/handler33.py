from telebot import TeleBot
from telebot.types import Message

from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from ..block21 import handler21
import getpath

path = getpath.pathreturn()

import createdb
from ..block34 import handler34
from ..block32 import handler32
from information_blocks.block33 import infohandler6

def loads(message, bot, aaaa):
    if message.text == "Примеры детских":
        infohandler6.infoblock9_0(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    if message.text == "▶️ Пропустить":
        createdb.exdb("NULL", 37, message.chat.id)
        handler34.block4_34(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    if message.text == "◀️ Назад":
        handler32.block4_32(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    bot.delete_message(message.chat.id, aaaa)
    createdb.exdb(message.text, 37, message.chat.id)
    handler34.block4_34(message, bot)
    

def block4_32(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(KeyboardButton("Примеры детских"))
    continue_btw = KeyboardButton("▶️ Пропустить")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(continue_btw, nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожалуйста, в ответном сообщении расскажите нам о своих пожеланиях к зоне детских.</b>\n\n"
        "<i>Если дополнительных идей пока нет или вы хотели бы обсудить этот пункт на личной встрече – пожалуйста, пропустите этот вопрос.</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
        
    
    


