from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery, InputMediaPhoto

import getpath

path = getpath.pathreturn()
    
cache = {}
def block4_40(message: Message, bot):

    markup = InlineKeyboardMarkup(row_width=1)
    pretty_bad = InlineKeyboardButton("Точность и расчёт", callback_data="tochno")
    bad = InlineKeyboardButton("Идеальное соответствие ожиданиям", callback_data="idealno")
    felllikegod = InlineKeyboardButton("Оптимальность строительства", callback_data="optimi")
    felllikegod2 = InlineKeyboardButton("Безопасность работы", callback_data="safety")
    felllikegod3 = InlineKeyboardButton("Персональный подход", callback_data="personal")

    media = [
        InputMediaPhoto(open('blocks/block73/1.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block73/2.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block73/3.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block73/4.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block73/5.jpg', 'rb'))
    ]
    data = bot.send_media_group(message.chat.id, media)
    cache[message.chat.id] = data

    markup.add(pretty_bad, bad, felllikegod, felllikegod2, felllikegod3)
    bot.send_message(message.chat.id, "<b>🔵 Самое важное в проектировании дома:</b>",
                         parse_mode="HTML",
                         reply_markup=markup)

    bot.delete_message(message.chat.id, message.id)
    

