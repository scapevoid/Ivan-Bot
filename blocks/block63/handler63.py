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
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_62")
    pretty_bad = InlineKeyboardButton("Подъездные пути в плохом состоянии", callback_data="very_bad")
    bad = InlineKeyboardButton("грунтовая дорога", callback_data="bad")
    pretty_good = InlineKeyboardButton("Дорога, отсыпанная щебнем", callback_data="good")
    good = InlineKeyboardButton("Дорога с твёрдым покрытием", callback_data="very_good")

    markup.add(pretty_bad, bad, pretty_good, good, back)
    a = bot.send_message(message.chat.id, "<b>🔵 Как обстоят дела с подъездом к участку?</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)    
    
    


