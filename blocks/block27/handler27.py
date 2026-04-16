from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery


from telebot.types import InputMediaPhoto
cache = {}
def block4_27(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_26")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_27")

    # определение данных 
    # [0] = определение что нужно сделать (выбрать)
    # [1] = дата -- которая хранится в text: str,
    # [2] = true or false 
    # [3] = данные о хандлере 
    # определение данных

    # если там сука выйдет ошибка тогда делаем на обычном тексте)))
    markup.add(InlineKeyboardButton("Спальня", callback_data="variant_data_0__27"))
    markup.add(InlineKeyboardButton("Отдельный санузел", callback_data="variant_data_1__27"))
    markup.add(InlineKeyboardButton("Гардеробная", callback_data="variant_data_2__27"))
    markup.add(InlineKeyboardButton("Приватная терраса", callback_data="variant_data_3__27"))



    markup.add(continue_btw, back)
    media = [
        InputMediaPhoto(open('blocks/block27/1.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block27/2.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block27/3.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block27/4.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block27/5.jpg', 'rb'))
    ]
    
    data = bot.send_media_group(message.chat.id, media)
    cache[message.chat.id] = data
    a = bot.send_message(message.chat.id, 
                          "<b>🔵Мастер-спальня — ваш личный оазис спокойствия!</b>\n\n"
                          "Здесь важна продуманная эргономика, умное зонирование и мягкое освещение.\n"
                          "Дополнить функционал можно зоной отдыха, гардеробной и отдельным санузлом.\n\n"
                          "<i>Ваше решение по наполнению этой зоны может быть не окончательным – мы ещё обсудим его вместе с командой.</i>\n\n"
                          "<b>Пожалуйста, отметьте все пункты, что планируете включить в пространство вашей мастер-спальни:</b>",
                          parse_mode="HTML",
                          reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)



    





        
    
    


