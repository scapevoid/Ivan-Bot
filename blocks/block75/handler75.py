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
        InputMediaPhoto(open('blocks/block75/1.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block75/2.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block75/3.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block75/4.jpg', 'rb'))
    ]
    data = bot.send_media_group(message.chat.id, media)
    cache[message.chat.id] = data
    markup = InlineKeyboardMarkup(row_width=1)
    pretty_bad = InlineKeyboardButton("Соответствие плану", callback_data="sootvetstvieplanu")
    bad = InlineKeyboardButton("Новый опыт", callback_data="newqualityoflife")
    felllikegod = InlineKeyboardButton("Реализовать цель", callback_data="realisegoals")
    felllikegod2 = InlineKeyboardButton("Минимум рисков", callback_data="miniriskiofbuild")




    markup.add(pretty_bad, bad, felllikegod, felllikegod2)
    a = bot.send_message(message.chat.id, "<b>🔵 Что в процессе строительства вы оцените выше всего?</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)
    
    


