from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery, InputFile

import asyncio





def block4_13_1(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    hleb = InlineKeyboardButton("Неоклассика", callback_data="neoclassic1")
    wright = InlineKeyboardButton("Стиль Райта", callback_data="wright1")
    hi_tech = InlineKeyboardButton("Hi-Tech", callback_data="hi_tech1")
    chale = InlineKeyboardButton("Шале", callback_data="chale1")
    barnhouse = InlineKeyboardButton("Барнхаус", callback_data="barnhouse1")
    scandinavian = InlineKeyboardButton("Скандинавский", callback_data="scandinavian1")
    unique = InlineKeyboardButton("Уникальный стиль", callback_data="unique1")
    markup.add(hleb, wright, hi_tech, chale, barnhouse, scandinavian, unique, InlineKeyboardButton("ℹ️Подробнее", callback_data="podrobnee1"))
    a = bot.send_photo(
        message.chat.id,
        InputFile("blocks/block13_1/8.jpg"),
        "<b>🔵Поговорим про архитектуру</b>\n\n"
        "От вашего выбора архитектурного стиля зависит внешний облик дома, размер окон, стилистика помещений, материалы и общий вайб.\n\n"
        "<b>▶️Узнайте больше о стилях в кнопке «Подробнее»</b>\n\n"
        "<i>Ваше решение может быть не окончательным – мы ещё обсудим его вместе с командой.</i>\n\n"
        "<b>Пожалуйста, выберите архитектурный стиль своего дома:</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)
        
    
    


