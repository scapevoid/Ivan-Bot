from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery, InputFile




def block4_46(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_45")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_46")
    markup.add(InlineKeyboardButton("Кабинет", callback_data="variant_data_0__46"))
    markup.add(InlineKeyboardButton("Мастерская", callback_data="variant_data_1__46"))
    markup.add(InlineKeyboardButton("Библиотека", callback_data="variant_data_2__46"))
    markup.add(InlineKeyboardButton("Зона не нужна", callback_data="zonanenuhasjhd"))
    markup.add(InlineKeyboardButton("ℹ️Подробнее", callback_data="podrobnee11"))



    markup.add(continue_btw, back)
    a = bot.send_photo(
        message.chat.id, InputFile("blocks/block46/prorab.jpg"),
        "<b>🔵Пространство для работы</b>\n\n"
        "Обсудим место, где рождаются идеи, принимаются важные решения и реализуется потенциал каждого члена семьи?\n\n"
        "Мы создадим функциональное и комфортное пространство, где вы будете наслаждаться процессом работы и достигать высоких результатов.\n\n"
        "<b>▶️Узнайте больше о функционале комнат в зоне работы в кнопке «Подробнее»</b>\n\n"
        "<b>Пожалуйста, отметьте, что войдёт в состав вашего домашнего пространства для работы и саморазвития:</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)



    





        
    
    


