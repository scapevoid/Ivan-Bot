from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from telebot.types import InputFile


def block4_23(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_221")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_23")

    # определение данных 
    # [0] = определение что нужно сделать (выбрать)
    # [1] = дата -- которая хранится в text: str,
    # [2] = true or false 
    # [3] = данные о хандлере 
    # определение данных

    # если там сука выйдет ошибка тогда делаем на обычном тексте)))
    markup.add(InlineKeyboardButton("Объединить кухню с гостиной", callback_data="variant_data_0__23"))
    markup.add(InlineKeyboardButton("Разделить кухню с гостиной", callback_data="variant_data_1__23"))
    markup.add(InlineKeyboardButton("Частично объединить", callback_data="variant_data_2__23"))
    markup.add(InlineKeyboardButton("Соединить гостиную с террасой", callback_data="variant_data_3__23"))



    markup.add(continue_btw, back)
    a = bot.send_photo(
        message.chat.id,InputFile("blocks/block23/dhear.jpg"),
        "🔵 <b>Сердце дома</b>\n\n"
        "В частном доме гостиная – это центральное пространство для семейного отдыха, приема гостей. Здесь собирается вся семья. Центральная часть дома должна быть функциональной, удобной, уютной и выражать характер владельцев.\n\n"
        "<b>Как вы планируете зонирование здесь?</b>\n\n"
        "<i>Это решение не обязательно должно быть окончательным – мы ещё обсудим его вместе с командой, и вы сможете прояснить все тонкости своего выбора.</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)
    


    





        
    
    


