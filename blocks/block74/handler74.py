from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery, InputMediaPhoto

from ..block21 import handler21
import getpath

path = getpath.pathreturn()

from ..block50 import handler50
    
cache = {}
def block4_40(message: Message, bot):
    media = [
        InputMediaPhoto(open('blocks/block74/1.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block74/2.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block74/3.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block74/4.jpg', 'rb')),
    ]
    data = bot.send_media_group(message.chat.id, media)
    cache[message.chat.id] = data
    markup = InlineKeyboardMarkup(row_width=1)
    pretty_bad = InlineKeyboardButton("Оптимальный баланс", callback_data="optimal")
    bad = InlineKeyboardButton("Высокий стандарт", callback_data="bigstandart")
    felllikegod = InlineKeyboardButton("Контроль затрат", callback_data="controlzatrat")
    felllikegod2 = InlineKeyboardButton("Это мой семейный оплот", callback_data="familybuild")



    markup.add(pretty_bad, bad, felllikegod, felllikegod2)
    a = bot.send_message(message.chat.id, "<b>🔵 Для чего вы строите дом?</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)
    
    


