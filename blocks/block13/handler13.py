from telebot import TeleBot
from telebot.types import Message
from telebot.types import InputFile
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

import asyncio





def block4_13(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    hleb = InlineKeyboardButton("Неоклассика", callback_data="neoclassic")
    wright = InlineKeyboardButton("Стиль Райта", callback_data="wright")
    hi_tech = InlineKeyboardButton("Hi-Tech", callback_data="hi_tech")
    chale = InlineKeyboardButton("Шале", callback_data="chale")
    barnhouse = InlineKeyboardButton("Барнхаус", callback_data="barnhouse")
    scandinavian = InlineKeyboardButton("Скандинавский", callback_data="scandinavian")
    unique = InlineKeyboardButton("Уникальный стиль", callback_data="unique")
    continue_btw = InlineKeyboardButton("Продолжить ▶️ ", callback_data="continue_121")
    markup.add(hleb, wright, hi_tech, chale, barnhouse, scandinavian, unique, continue_btw)
    a = bot.send_message(
        message.chat.id,
        "<b>🔵 Архитектура – это про вас</b>\n\n"
        "Если ваш проект выполняет команда IVAN DOM – вам не придётся разбираться в тонкостях архитектурных стилей – это работа архитекторов.\n\n"
        "Но вы можете выбрать близкий вам по духу и образу жизни. Или тот, что привлекает вас эстетически.\n\n"
        "Или собрать лучшие черты разных стилей в собственный авторский замысел. А мы поможем совместить ваш выбор с функционалом будущего дома и запланированным бюджетом.\n\n"
        "<b>Рассказали простыми словами об архитектурных стилях, которые чаще всего выбирают наши заказчики:</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)
        
    
    


