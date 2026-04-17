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
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_65")
    pretty_bad = InlineKeyboardButton("Нет", callback_data="isnotis")
    sadf = InlineKeyboardButton("Не знаю", callback_data="isnotidk")
    bad = InlineKeyboardButton("Есть", callback_data="isyesis")

    markup.add(pretty_bad, sadf, bad, back)
    a = bot.send_message(message.chat.id, "<b>🔵Есть ли у участка ограничения на строительство по градостроительному плану?</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)   
    
    


