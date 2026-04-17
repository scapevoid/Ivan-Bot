from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery, InputMediaPhoto

import getpath

path = getpath.pathreturn()


    
cache = {}
def block4_40_1(message: Message, bot):
    media = [
        InputMediaPhoto(open('blocks/block73_5/1.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block73_5/2.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block73_5/3.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block73_5/4.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block73_5/5.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block73_5/6.jpg', 'rb'))
    ]
    data = bot.send_media_group(message.chat.id, media)
    cache[message.chat.id] = data
    markup = InlineKeyboardMarkup(row_width=1)
    pretty_bad = InlineKeyboardButton("Надёжность и долговечность", callback_data="nadejnostiidolgovechins")
    bad = InlineKeyboardButton("Экономия бюджета", callback_data="ekomonia")
    felllikegod = InlineKeyboardButton("Ценность времени", callback_data="wennhosidhtvtyyb")
    felllikegod2 = InlineKeyboardButton("Гарантия качества", callback_data="garantayadsfasdfasdf")
    felllikegod3 = InlineKeyboardButton("Выбор профессионалов", callback_data="viborprofifff")
    felllikegod4 = InlineKeyboardButton("Ответственность строителей", callback_data="a65465asdfasdf")

    markup.add(pretty_bad, bad, felllikegod, felllikegod2, felllikegod3, felllikegod4)
    bot.send_message(
        message.chat.id,
        "🔵 <b>Что для вас самое важное в процессе строительства дома?</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)
