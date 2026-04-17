from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery
from telebot.types import InputFile



def block4_46(message: Message, bot):

    markup = InlineKeyboardMarkup(row_width=1)
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_455")

    markup.add(InlineKeyboardButton("Кабинет", callback_data="cabinet"))
    markup.add(InlineKeyboardButton("Мастерская", callback_data="masterskaya"))
    markup.add(InlineKeyboardButton("Библиотека", callback_data="biblioteka"))
    



    markup.add(continue_btw)
    a = bot.send_message(
        message.chat.id,
        "<b>🔵Второе имя этой зоны – «личная эффективность»</b>\n\n"
        "В этом функциональном и комфортном пространстве вы будете наслаждаться процессом работы и достигать высоких результатов. Или наоборот – выражать себя в творчестве и кайфовать от процесса.\n\n"
        "<b>Узнайте подробнее о вариантах наполнения этой локации в доме:</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)



    





        
    
    


