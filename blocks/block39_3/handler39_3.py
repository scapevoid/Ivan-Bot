from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery




def block4_39(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_38")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_39")

    # определение данных 
    # [0] = определение что нужно сделать (выбрать)
    # [1] = дата -- которая хранится в text: str,
    # [2] = true or false 
    # [3] = данные о хандлере 
    # определение данных

    # если там сука выйдет ошибка тогда делаем на обычном тексте)))
    markup.add(InlineKeyboardButton("Ванна", callback_data="variant_data_0__393"))
    markup.add(InlineKeyboardButton("Душ", callback_data="variant_data_1__393"))
    markup.add(InlineKeyboardButton("Тропический душ", callback_data="variant_data_2__393"))
    markup.add(InlineKeyboardButton("Раковина", callback_data="variant_data_3__393"))
    markup.add(InlineKeyboardButton("Двойная раковина", callback_data="variant_data_4__393"))
    markup.add(InlineKeyboardButton("Унитаз", callback_data="variant_data_5__393"))
    markup.add(InlineKeyboardButton("Биде", callback_data="variant_data_6__393"))
    markup.add(InlineKeyboardButton("Гигиенический душ", callback_data="variant_data_7__39"))



    markup.add(continue_btw, back)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожалуйста, выберите наполнение санузла №1</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)



    





        
    
    


