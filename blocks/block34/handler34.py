from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery




def block4_34(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_33")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_34")

    # определение данных 
    # [0] = определение что нужно сделать (выбрать)
    # [1] = дата -- которая хранится в text: str,
    # [2] = true or false 
    # [3] = данные о хандлере 
    # определение данных

    # если там сука выйдет ошибка тогда делаем на обычном тексте)))
    markup.add(InlineKeyboardButton("Одна гостевая", callback_data="variant_data_0__34"))
    markup.add(InlineKeyboardButton("Две гостевые", callback_data="variant_data_1__34"))
    markup.add(InlineKeyboardButton("Дополнительный санузел", callback_data="variant_data_2__34"))
    markup.add(InlineKeyboardButton("Эта зона не потребуется", callback_data="skip3_4"))


    markup.add(continue_btw, back)
    a = bot.send_message(
        message.chat.id,
        "<b>🔵Зона для гостей</b>\n\n"
        "Зона гостевых в частном доме предназначена для комфортного размещения ваших близких. Она обеспечивает им уединение и место для отдыха, не нарушая при этом приватность хозяев.\n\n"
        "<b>Пожалуйста, отметьте, какие помещения необходимы вам в гостевой зоне:</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)



    





        
    
    


