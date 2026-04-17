from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()

from ..block52 import handler52
from ..block50 import handler50
import time
import createdb
from information_blocks.block51 import infohandler6

def loads(message, bot, aa):
    if message.text == "Примеры хозяйственной зоны":
        infohandler6.infoblock9_0(message, bot)
        bot.delete_message(message.chat.id, aa) 
    if message.text == "◀️ Назад":
        handler50.block4_40(message, bot)
        bot.delete_message(message.chat.id, aa) 
        return
    bot.delete_message(message.chat.id, aa) 
    createdb.exdb(message.text, 57, message.chat.id)
    handler52.block4_52(message, bot)
    

def block4_40(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    primer = KeyboardButton("Примеры хозяйственной зоны")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(primer, nazad)

    a = bot.send_message(message.chat.id, "<b>🔵Пожалуйста, в ответном сообщении расскажите нам о своих пожеланиях к хозяйственно-бытовой зоне.</b> \n\n"
                         "<i>Если дополнительных идей пока нет или вы хотели бы обсудить этот пункт на личной встрече с нашей командой – пожалуйста, пропустите этот вопрос.</i>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id) 

    
    


