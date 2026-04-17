from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery
from telebot.types import InputFile


cache37 = {}
def block4_52(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_522")

    markup.add(InlineKeyboardButton("Бар / Кальянная / Сигарная", callback_data="vinnaya"))
    markup.add(InlineKeyboardButton("Оружейная", callback_data="oruheynaya"))
    markup.add(InlineKeyboardButton("Сейфовая", callback_data="seyfovata"))
    markup.add(InlineKeyboardButton("Трофейная / Музей / Галерея", callback_data="tropheynaya"))
    markup.add(InlineKeyboardButton("Бассейн/СПА в доме", callback_data="SPAzonavnutri"))
    markup.add(InlineKeyboardButton("Спорт-зона/ Бильярд/ Гейм-зона", callback_data="sportivnaytazona"))
    markup.add(InlineKeyboardButton("Кинозал", callback_data="kinozal"))
    markup.add(InlineKeyboardButton("Приватная комната для взрослых", callback_data="privatnaya"))






    markup.add(continue_btw)
    a = bot.send_message(
        message.chat.id,
        "<b>🔵 Такое – только у вас!</b>\n\n"
        "Будем честны – дома строят именно для воплощения своих идей.\n"
        "Кто-то мечтает о зимнем саде, другие – о месте для своей коллекции.\nНаверняка и у вас есть своя идея «комнаты мечты».\n\n"
        "<b>Вот несколько вдохновляющих идей, чтобы сделать будущий дом лично вашей историей:</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)
    messages = cache37.get(message.chat.id, [])
    for msg in messages:
        bot.delete_message(message.chat.id, msg.message_id)



    





        
    
    


