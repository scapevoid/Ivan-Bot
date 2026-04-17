from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove, InputFile

from telebot.types import CallbackQuery
from ..block54.handler54 import cache as cache34



def block4_54(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_535")
    markup.add(InlineKeyboardButton("Терраса у дома", callback_data="terrasaudoma"))
    markup.add(InlineKeyboardButton("Крыльцо", callback_data="krilcho"))
    markup.add(InlineKeyboardButton("Навес для авто, примыкающий к дому", callback_data="navesavtoprim"))
    markup.add(InlineKeyboardButton("Навес для авто отдельностоящий", callback_data="navesavto"))
    markup.add(InlineKeyboardButton("Гараж, примыкающий к дому", callback_data="garahprim"))
    markup.add(InlineKeyboardButton("Гараж отдельностоящий", callback_data="garahotdel"))
    markup.add(InlineKeyboardButton("Доп. гараж", callback_data="dopgaraj"))
    markup.add(InlineKeyboardButton("Гостевая парковка", callback_data="gostevayaparkovka"))
    






    markup.add(continue_btw)
    a = bot.send_photo(
        message.chat.id,
        InputFile("blocks/block53_5/1.jpg"),
        "<b>🔵 Строения дополнительные, а комфорт – главный!</b>\n\n"
        "Они делают вашу жизнь в доме ещё удобнее, а участок – функциональнее.\n\n"
        "<b>Узнайте подробнее о самых популярных постройках на участке:</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)
    messages = cache34.get(message.chat.id, [])
    for msg in messages:
        bot.delete_message(message.chat.id, msg.message_id)



    





        
    
    


