from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()

from ..block50 import handler50


    

def block4_40(message: Message, bot):
    

    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_57")
    yes = InlineKeyboardButton("Да", callback_data="yes_buyed")
    no = InlineKeyboardButton("Нет", callback_data="not_buyed")
    asd = InlineKeyboardButton("Нет, нужна помощь", callback_data="not_need_help")
    markup.add(yes, no, asd, back)

    # 52 пропускаем до 53 :heart: :sungalsees:
    a = bot.send_message(message.chat.id, "<b>🔵 У вас уже приобретён участок?</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)
    
    


