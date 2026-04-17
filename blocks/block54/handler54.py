from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery, InputMediaPhoto



cache = {}

def block4_54(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_534")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_54")
    markup.add(InlineKeyboardButton("Терраса у дома", callback_data="variant_data_0__54"))
    markup.add(InlineKeyboardButton("Крыльцо", callback_data="variant_data_1__54"))
    markup.add(InlineKeyboardButton("Навес для авто, примыкающий к дому", callback_data="variant_data_2__54"))
    markup.add(InlineKeyboardButton("Навес для авто отдельностоящий", callback_data="variant_data_3__54"))
    markup.add(InlineKeyboardButton("Гараж, примыкающий к дому", callback_data="variant_data_4__54"))
    markup.add(InlineKeyboardButton("Гараж отдельностоящий", callback_data="variant_data_5__54"))
    markup.add(InlineKeyboardButton("Доп. гараж", callback_data="variant_data_6__54"))
    markup.add(InlineKeyboardButton("Гостевая парковка", callback_data="variant_data_7__54"))
    markup.add(InlineKeyboardButton("Зона не нужна", callback_data="asdfasfzonaasdfadsf"))
    markup.add(InlineKeyboardButton("ℹ️Подробнее", callback_data="podrobnee8"))
    

    media = [
        InputMediaPhoto(open('blocks/block54/1.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block54/2.jpg', 'rb')),
        InputMediaPhoto(open('blocks/block54/3.png', 'rb'))
    ]
    data = bot.send_media_group(message.chat.id, media)
    cache[message.chat.id] = data
    markup.add(continue_btw, back)
    a = bot.send_message(
        message.chat.id,
        "<b>🔵 Планируем участок</b>\n\n"
        "Детально проработанное пространство участка повышает комфорт вашей жизни.\n\n"
        "Вы наслаждаетесь цветущим садом, занимаетесь спортом или собираете близких на барбекю в уютной беседке, пока дети безопасно играют на свежем воздухе.\n\n"
        "<b>▶️Узнайте больше о возможностях вашего двора в кнопке «Подробнее»</b>\n\n"
        "<b>Пожалуйста, выберите все объекты базового комфорта, необходимые вам на участке:</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)


    





        
    
    


