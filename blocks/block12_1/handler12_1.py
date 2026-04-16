from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block13 import handler13
import getpath

path = getpath.pathreturn()

def block4_12_1(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_12")
    hleb = InlineKeyboardButton("Хорошая идея, рассмотрю", callback_data="basement_yes")
    batton = InlineKeyboardButton("Скорее нет", callback_data="basement_probably_no")
    button = InlineKeyboardButton("Точно нет", callback_data="basement_definitely_no")
    info = InlineKeyboardButton("Узнать подробнее про цоколь", callback_data="basement_info")

    markup.add(hleb, batton, button, info, back)
    a = bot.send_message(message.chat.id, "<b>🔵 Будет ли в доме цокольный этаж?</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)