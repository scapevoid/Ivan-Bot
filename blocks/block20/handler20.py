from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery


from ..block19_1 import handler19_1
import getpath
from information_blocks.block9 import infohandler6

path = getpath.pathreturn()

import createdb


def loads(message, bot, aa):
    if message.text == "▶️ Пропустить":
        createdb.exdb("NULL", 22, message.chat.id)
        infohandler6.infoblock9_0(message, bot)
        bot.delete_message(message.chat.id, aa)
        return
    if message.text == "◀️ Назад":
        handler19_1.block4_9(message, bot)
        bot.delete_message(message.chat.id, aa)
        return
    bot.delete_message(message.chat.id, aa)
    createdb.exdb(message.text, 22, message.chat.id)
    infohandler6.infoblock9_0(message, bot)

def block4_11(message: Message, bot):
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    continue_btw = KeyboardButton("▶️ Пропустить")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(continue_btw, nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожелания к кровле</b>\n\n"
        "<b>Пожалуйста, в ответном сообщении расскажите нам о своих особых пожеланиях к кровле будущего дома.</b>\n\n"
        "<i>Если дополнительных идей пока нет или вы хотели бы обсудить этот пункт на личной встрече с нашей командой – просто пропустите этот вопрос.</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
    
    


