from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove, InputFile

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()
import time
from information_blocks.block10_5 import infohandler10_5
from ..block53_2 import handler54_2
from ..block53 import handler53
import createdb
def loads(message, bot, aa):
    if message.text == "▶️ Пропустить":
        createdb.exdb("NULL", 60, message.chat.id)
        handler54_2.block4_53(message, bot)
        bot.delete_message(message.chat.id, aa)
        return
    if message.text == "◀️ Назад":
        handler53.block4_53(message, bot)
        bot.delete_message(message.chat.id, aa)
        return
    bot.delete_message(message.chat.id, aa)
    createdb.exdb(message.text, 60, message.chat.id)
    handler54_2.block4_53(message, bot)



def block4_53(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    continue_btw = KeyboardButton("▶️ Пропустить")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(KeyboardButton("300 – 350 мм (2 ступени на входе)"))
    markup.add(KeyboardButton("350 – 450 мм (3 ступени на входе)"))
    markup.add(KeyboardButton("450 – 600 мм (4 ступени на входе)"))
    markup.add(KeyboardButton("600 – 800 мм (5 ступеней на входе)"))
    markup.add(KeyboardButton("более 800 мм (на входе 6 ступеней и более)"))

    markup.add(continue_btw, nazad)
    a = bot.send_photo(message.chat.id, 
                       InputFile("blocks/block53_1/10.jpg"),
                       "<b>🔵Габариты и размеры дома</b>\n\n"
                       "<i>Пожалуйста, укажите комфортный для вас уровень чистового пола первого этажа</i>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)   
    
    


