from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery




def block4_46(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_63")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_65")
    markup.add(InlineKeyboardButton("Вода", callback_data="variant_data_0__65"))
    markup.add(InlineKeyboardButton("Электроэнергия", callback_data="variant_data_1__65"))
    markup.add(InlineKeyboardButton("Газ", callback_data="variant_data_2__65"))
    markup.add(InlineKeyboardButton("Канализация", callback_data="variant_data_3__65"))
    markup.add(InlineKeyboardButton("Высокоскоростной интернет", callback_data="variant_data_4__65"))
    





    markup.add(continue_btw, back)
    a = bot.send_message(message.chat.id, "<b>🔵 Какие коммуникации есть/ проходят по меже участка?</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)


    





        
    
    


