from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery




def block4_31(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_30")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_31")
    markup.add(InlineKeyboardButton("Игровая комната", callback_data="variant_data_0__31"))
    markup.add(InlineKeyboardButton("Комната для занятий", callback_data="variant_data_1__31"))
    markup.add(InlineKeyboardButton("Гардеробная", callback_data="variant_data_2__31"))
    markup.add(InlineKeyboardButton("Детский санузел", callback_data="variant_data_3__31"))
    markup.add(InlineKeyboardButton("Не нужно доп комнат", callback_data="pppioiipiasdfadf"))
    markup.add(InlineKeyboardButton("ℹ️Подробнее", callback_data="podrobnee6"))



    markup.add(continue_btw, back)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Зона детских</b>\n\n"
        "Это не только пространство для сна и отдыха. Здесь дети играют, учатся, принимают гостей, развивают самостоятельность и во всех смыслах растут.\n\n"
        "Это их собственная часть дома. Особенно, когда дети – уже не малыши.\n\n"
        "<b>▶️Узнайте больше о функционале комнат в зоне детских в кнопке «Подробнее»</b>\n\n"
        "<b>Пожалуйста, отметьте, какие ещё комнаты вы планируете в зоне детских:</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)


    





        
    
    


