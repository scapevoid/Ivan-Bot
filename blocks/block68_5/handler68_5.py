from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()

from ..block50 import handler50

    

def block4_40(message: Message, bot):
    
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_67")
    pretty_bad = InlineKeyboardButton("Нет", callback_data="notisnotisnotasd")
    bad = InlineKeyboardButton("Да", callback_data="yesisyesisyesasd")

    markup.add(pretty_bad, bad, back)
    a = bot.send_message(message.chat.id, "<b>🔵 Выполнена ли топосъемка для данного участка?</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)
    
    


