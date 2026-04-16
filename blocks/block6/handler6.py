from telebot import TeleBot
from telebot.types import Message
import time

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery


from ..block7 import handler7
from ..block4_6 import handler4_6
import getpath
path = getpath.pathreturn()
import createdb

def loads(message, bot, aa):
    if message.text == "▶️ Пропустить":
        createdb.exdb("NULL", 8, message.chat.id)

        
        bot.delete_message(message.chat.id, aa)
        handler7.block4_7(message, bot)
        return
    if message.text == "◀️ Назад":
        handler4_6.block4_5(message, bot)
        bot.delete_message(message.chat.id, aa)
        return
    bot.delete_message(message.chat.id, aa)
    createdb.exdb(message.text, 8, message.chat.id)

    handler7.block4_7(message, bot)
    

def block4_6(message: Message, bot):
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    continue_btw = KeyboardButton("▶️ Пропустить")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(continue_btw, nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Расскажите о важном</b>\n\n"
        "Пожалуйста, в ответном сообщении поделитесь тем, что ещё максимально важно для вас в новом доме.\n\n"
        "<i>Ваши пожелания помогут нам создать дом, который будет полностью соответствовать вашим ожиданиям и потребностям.</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda asd: loads(asd, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
    


        
    
    


