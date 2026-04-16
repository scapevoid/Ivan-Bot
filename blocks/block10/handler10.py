from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery, InputFile


from ..block11 import handler11
    

def block4_10(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_8")
    biznes = InlineKeyboardButton("Бизнес-класс", callback_data="biznes1")
    comfort = InlineKeyboardButton("Комфорт-класс", callback_data="comfort1")
    premium = InlineKeyboardButton("Премиум-класс", callback_data="premium1")
    markup.add(comfort, biznes, premium, InlineKeyboardButton("Подробнее", callback_data="podrobnee22"), back)
    a = bot.send_photo(message.chat.id, InputFile("blocks/block10/6.1.jpg"), "<b>🔵 Выберите нужный класс комфорта</b>\n\n"
                         "С категорией комфорта важно определиться до старта работ – так мы сбалансируем ваши пожелания и бюджет, а вы вложите в свой дом сумму точно по договору и ни рублём больше.\n\n"
                         "▶️Узнайте больше о классах домов от IVAN DOM в кнопке «Подробнее»\n\n"
                         "<b>Какую категорию вы рассматриваете для своего дома?</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)
    
        
    
    


