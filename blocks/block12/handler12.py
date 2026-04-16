from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery



    
    

def block4_12(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_11")
    hleb = InlineKeyboardButton("Рассматриваю одноэтажные", callback_data="onefloor")
    batton = InlineKeyboardButton("Два полноценных этажа", callback_data="twofullfloor")
    button = InlineKeyboardButton("Нравятся дома с мансардами", callback_data="mansard")
    buttonchik = InlineKeyboardButton("Обсудим с архитектором", callback_data="after_architect")

    markup.add(hleb, batton, button, buttonchik, back)
    a = bot.send_message(message.chat.id, "<b>🔵 Какой этажности будет дом?</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)
        
    
    


