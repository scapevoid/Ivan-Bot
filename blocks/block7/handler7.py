from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery



def block4_7(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_6")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_7")

    # определение данных 
    # [0] = определение что нужно сделать (выбрать)
    # [1] = дата -- которая хранится в text: str,
    # [2] = true or false 
    # [3] = данные о хандлере 
    # определение данных

    # если там сука выйдет ошибка тогда делаем на обычном тексте)))
    markup.add(InlineKeyboardButton("Владелец дома", callback_data="variant_data_0__7"))
    markup.add(InlineKeyboardButton("Владелица дома", callback_data="variant_data_1__7"))
    markup.add(InlineKeyboardButton("Ребёнок/дети", callback_data="variant_data_2__7"))
    markup.add(InlineKeyboardButton("Родители владельцев", callback_data="variant_data_3__7"))
    markup.add(InlineKeyboardButton("Будущие внуки и правнуки", callback_data="variant_data_4__7"))
    markup.add(InlineKeyboardButton("Периодические гости", callback_data="variant_data_5__7"))
    markup.add(InlineKeyboardButton("Любимый питомец", callback_data="variant_data_6__7"))


    markup.add(continue_btw, back)
    a = bot.send_message(message.chat.id, "<b>🔵Кто будет жить в будущем доме?\n\nПожалуйста, отметьте все нужные пункты:</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)



    





        
    
    


