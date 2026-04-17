from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()

from ..block76 import handler76
import createdb
import os

    

def block4_40(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton(text="Связаться с IVAN DOM", url="https://t.me/IDRmanager"))
    markup.add(InlineKeyboardButton("Финальное видео", url="https://rutube.ru/video/private/eb64012edabc9cb9dad9b06d1ecb365e/?p=W4UVdj3-4EbzFamwtl9Cig"))
    markup.add(InlineKeyboardButton("Отправить анкету", callback_data="send_anket"))
    markup.add(InlineKeyboardButton("◀️ Назад", callback_data="return_76"))
    a = bot.send_message(message.chat.id, 
    "<b>🔵Благодарим вас за вдумчивый подход к мечте о собственном доме!</b>\n\n"
    "Наш проектный отдел только что получил в работу информацию о вашем будущем доме  и уже начал подбор лучших решений по концепции и планировкам.\n\n"
    "В ближайшее время мы попросим вас согласовать время встречи, где обсудим этапы, сроки и предварительный бюджет проекта.\n\n"
    "Если у вас возникли вопросы, пожалуйста, свяжитесь с нами по номеру <b>8 (863) 256 44 88</b>\n\n"
    "Мы на связи!\n\n"
    "<b><i>С уважением, Иван Чернявский и команда IVAN DOM Rostov</i></b>", 
    reply_markup=markup, parse_mode="HTML")
    bot.delete_message(message.chat.id, message.id)
    
    


