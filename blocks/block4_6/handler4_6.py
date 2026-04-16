from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery




def block4_5(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_451")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_464")

    # определение данных 
    # [0] = определение что нужно сделать (выбрать)
    # [1] = дата -- которая хранится в text: str,
    # [2] = true or false 
    # [3] = данные о хандлере 
    # определение данных

    # если там сука выйдет ошибка тогда делаем на обычном тексте)))
    markup.add(InlineKeyboardButton("Образ дома отражает мой стиль и вкус", callback_data="variant_data_0__464"))
    markup.add(InlineKeyboardButton("Тишина и уединение, спокойствие", callback_data="variant_data_1__464"))
    markup.add(InlineKeyboardButton("Приватность каждого члена семьи", callback_data="variant_data_2__464"))
    markup.add(InlineKeyboardButton("Эргономика: дом удобен для жизни", callback_data="variant_data_3__464"))
    markup.add(InlineKeyboardButton("Много вариантов досуга с семьёй", callback_data="variant_data_4__464"))
    markup.add(InlineKeyboardButton("Практичность и функционал планировок", callback_data="variant_data_5__464"))
    markup.add(InlineKeyboardButton("Энергоэффективность и экологичность", callback_data="variant_data_6__464"))
    markup.add(InlineKeyboardButton("Безопасность, технологичность", callback_data="variant_data_7__464"))

    markup.add(continue_btw, back)
    a = bot.send_message(message.chat.id, "<b>🔵 Что для вас наиболее ценно и важно в доме?</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)


    





        
    
    


