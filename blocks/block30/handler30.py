from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block13 import handler13


    
    

def block4_30(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_29")
    hleb = InlineKeyboardButton("1", callback_data="oneroom")
    batton = InlineKeyboardButton("2", callback_data="tworooms")
    button = InlineKeyboardButton("3", callback_data="threerooms")
    buttonchik = InlineKeyboardButton("Эта зона не потребуется", callback_data="thiszoneisnotneeded")
    # note 25 цифра для записи то есть мы сейчас пишем 26
    markup.add(hleb, batton, button, buttonchik, back)
    a = bot.send_message(message.chat.id, "<b>🔵 Сколько комнат вы планируете в зоне детских?</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)
        
    
    


