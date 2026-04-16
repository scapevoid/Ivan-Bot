from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery




def block4_5(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_4")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_5")

    # определение данных 
    # [0] = определение что нужно сделать (выбрать)
    # [1] = дата -- которая хранится в text: str,
    # [2] = true or false 
    # [3] = данные о хандлере 
    # определение данных

    # если там сука выйдет ошибка тогда делаем на обычном тексте)))
    markup.add(InlineKeyboardButton("Выразить себя в дизайне и архитектуре", callback_data="variant_data_0__5"))
    markup.add(InlineKeyboardButton("Создать дом c wow-эффектом", callback_data="variant_data_1__5"))
    markup.add(InlineKeyboardButton("Создать пространство для отдыха", callback_data="variant_data_2__5"))
    markup.add(InlineKeyboardButton("Дом, удобный в эксплуатации", callback_data="variant_data_3__5"))
    markup.add(InlineKeyboardButton("Дом с возможностью модернизации", callback_data="variant_data_4__5"))
    markup.add(InlineKeyboardButton("Жизнь по моим правилам", callback_data="variant_data_5__5"))


    markup.add(continue_btw, back)
    a = bot.send_message(message.chat.id, "<b>🔵 Давайте уточним, какие еще результаты важны вам в строительстве?</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)


    





        
    
    


