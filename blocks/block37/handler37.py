from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block13 import handler13


    
    

def block4_37(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_36")
    hleb = InlineKeyboardButton("2", callback_data="bathroom_two")
    batton = InlineKeyboardButton("3", callback_data="bathroom_three")
    button = InlineKeyboardButton("4 и более", callback_data="bathroom_four_and_more")
    # note 31 цифра для записи то есть мы сейчас пишем 32
    markup.add(hleb, batton, button, InlineKeyboardButton("Примеры санузлов", callback_data="asdfsafasdfasdf"), back)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Сколько планируете санузлов в доме, включая туалетные, ванные комнаты и душевые?</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)
        
    
    


