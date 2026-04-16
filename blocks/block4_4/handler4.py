from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery


from ..block4_5 import handler5


def block4_4(message: Message, bot):
    
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_3")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_4")

    # определение данных 
    # [0] = определение что нужно сделать (выбрать)
    # [1] = дата -- которая хранится в text: str,
    # [2] = true or false 
    # [3] = данные о хандлере 
    # определение данных

    # если там сука выйдет ошибка тогда делаем на обычном тексте)))
    markup.add(InlineKeyboardButton("Создать комфорт для семьи", callback_data="variant_data_0__4"))
    markup.add(InlineKeyboardButton("Реализовать давнюю мечту", callback_data="variant_data_1__4"))
    markup.add(InlineKeyboardButton("Увеличить пространство для жизни", callback_data="variant_data_2__4"))
    markup.add(InlineKeyboardButton("Повысить качество жизни", callback_data="variant_data_3__4"))
    markup.add(InlineKeyboardButton("Рационально использовать бюджет", callback_data="variant_data_4__4"))
    markup.add(InlineKeyboardButton("Обеспечить надёжность дома на годы", callback_data="variant_data_5__4")) 
    markup.add(continue_btw, back)
    a = bot.send_message(message.chat.id, "<b>🔵 Выберите самые важные цели вашего строительства</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)

    





        
    
    


