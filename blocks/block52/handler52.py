from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery, InputFile




def block4_52(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_51")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_52")

    markup.add(InlineKeyboardButton("Бар / Кальянная / Сигарная", callback_data="variant_data_0__52"))
    markup.add(InlineKeyboardButton("Оружейная", callback_data="variant_data_1__52"))
    markup.add(InlineKeyboardButton("Сейфовая", callback_data="variant_data_2__52"))
    markup.add(InlineKeyboardButton("Трофейная / Музей / Галерея", callback_data="variant_data_3__52"))
    markup.add(InlineKeyboardButton("Бассейн/СПА в доме", callback_data="variant_data_4__52"))
    markup.add(InlineKeyboardButton("Спорт-зона / Бильярд / Гейм-зона", callback_data="variant_data_5__52"))
    markup.add(InlineKeyboardButton("Кинозал", callback_data="variant_data_6__52"))
    markup.add(InlineKeyboardButton("Приватная комната для взрослых", callback_data="variant_data_7__52"))
    markup.add(InlineKeyboardButton("Зона не нужна", callback_data="zonasdflkasljdfklasjf"))
    markup.add(InlineKeyboardButton("ℹ️Подробнее", callback_data="podrobnee7"))
    






    markup.add(continue_btw, back)
    a = bot.send_photo(message.chat.id, InputFile("blocks/block52/prost.jpg"),
                         "<b>🔵Планируем зону эмоций</b>\n\n"
                         "У вас есть комната мечты? Давайте её построим! Ведь главный кайф жизни в частном доме — игра по своим правилам.\n\n"
                         "<b>▶️Узнайте больше о возможностях вашего дома в кнопке «Подробнее»</b>\n\n"
                         "<b>Какие пространства с необычными функциями вы хотели бы запланировать в своём доме?</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)



    





        
    
    


