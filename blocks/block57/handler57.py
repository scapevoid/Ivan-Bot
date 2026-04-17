from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()

from information_blocks.block58 import infohandler11
from ..block56 import handler56
import createdb
def loads(message, bot, aa):
    if message.text == "▶️ Пропустить":
        createdb.exdb("NULL", 67, message.chat.id)
        infohandler11.infoblock10_5(message, bot)
        bot.delete_message(message.chat.id, aa)
        return
    if message.text == "◀️ Назад":
        bot.delete_message(message.chat.id, aa)
        handler56.block4_56(message, bot)
    bot.delete_message(message.chat.id, aa)
    createdb.exdb(message.text, 67, message.chat.id)
    infohandler11.infoblock10_5(message, bot)
    

def block4_57(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    continue_btw = KeyboardButton("▶️ Пропустить")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(continue_btw, nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожалуйста, в ответном сообщении расскажите нам о своих пожеланиях и идеях по организации пространства вокруг дома.</b>\n\n"
        "<i>Если дополнительных идей пока нет или вы хотели бы обсудить этот пункт на личной встрече с нашей командой  – пожалуйста, пропустите этот вопрос.</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)    
    
    


