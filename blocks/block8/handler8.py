from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery


from ..block7 import handler7
from ..block9 import handler9
import getpath
import createdb
path = getpath.pathreturn()
from information_blocks.block6_3 import infohandler6_3

def loads(message, bot, idaa):
    if message.text == "▶️ Пропустить":
        createdb.exdb("NULL", 10, message.chat.id)

        infohandler6_3.infoblock6_3(message, bot)
        bot.delete_message(message.chat.id, idaa)
        return
    if message.text == "◀️ Назад":
        handler7.block4_7(message, bot)
        bot.delete_message(message.chat.id, idaa)
        return
    createdb.exdb(message.text, 10, message.chat.id)
    infohandler6_3.infoblock6_3(message, bot)
    bot.delete_message(message.chat.id, idaa)
    

def block4_8(message: Message, bot):
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    continue_btw = KeyboardButton("▶️ Пропустить")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(continue_btw, nazad)
    a = bot.send_message(message.chat.id, "<b>🔵Пожалуйста, в ответном сообщении расскажите, кто ещё будет проживать в вашем новом доме</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
        
    
    


