from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block54.handler54 import cache as cache37


def block4_55(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_565")

    # определение данных 
    # [0] = определение что нужно сделать (выбрать)
    # [1] = дата -- которая хранится в text: str,
    # [2] = true or false 
    # [3] = данные о хандлере 
    # определение данных

    # если там сука выйдет ошибка тогда делаем на обычном тексте)))
    markup.add(InlineKeyboardButton("Беседка — Открытая беседка", callback_data="besetka"))
    markup.add(InlineKeyboardButton("Зона огня", callback_data="zonaognya"))
    markup.add(InlineKeyboardButton("Релакс-зона", callback_data="relaxzona"))
    markup.add(InlineKeyboardButton("Баня / СПА", callback_data="banyaspa"))
    markup.add(InlineKeyboardButton("Детская площадка", callback_data="detskayaplashadka"))
    markup.add(InlineKeyboardButton("Спортивная площадка", callback_data="sportivna"))
    markup.add(InlineKeyboardButton("Гостевой домик", callback_data="gostevoydomik"))
    






    markup.add(continue_btw)
    a = bot.send_message(message.chat.id, "<b>🔵Дольче вита в вашем дворе</b>\n\n"
                         "Экспертный подход к планировке участка даёт владельцу дома возможность использовать его потенциал на 200%\n\n"
                         "<b>Узнайте подробнее, какие объекты могут быть в зоне отдыха на вашем участке:</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)
    messages = cache37.get(message.chat.id, [])
    for msg in messages:
        bot.delete_message(message.chat.id, msg.message_id)


    





        
    
    


