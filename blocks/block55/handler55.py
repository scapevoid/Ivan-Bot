from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block54.handler54 import cache as cache37


def block4_55(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_54")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_55")
    markup.add(InlineKeyboardButton("Беседка — Открытая беседка", callback_data="variant_data_0__55"))
    markup.add(InlineKeyboardButton("Зона огня", callback_data="variant_data_1__55"))
    markup.add(InlineKeyboardButton("Релакс-зона", callback_data="variant_data_2__55"))
    markup.add(InlineKeyboardButton("Баня / СПА", callback_data="variant_data_3__55"))
    markup.add(InlineKeyboardButton("Детская площадка", callback_data="variant_data_4__55"))
    markup.add(InlineKeyboardButton("Спортивная площадка", callback_data="variant_data_5__55"))
    markup.add(InlineKeyboardButton("Гостевой домик", callback_data="variant_data_6__55"))
    markup.add(InlineKeyboardButton("Зона не нужна", callback_data="asdfasfzonaaasassdfadsf"))
    markup.add(InlineKeyboardButton("ℹ️Подробнее", callback_data="podrobnee10"))






    markup.add(continue_btw, back)
    a = bot.send_message(message.chat.id, "<b>🔵Отдых и перезагрузка</b>\n\n"
                         "Зона отдыха во дворе дома – возможность насладиться вашей личной частичкой природы, расслабиться и набраться сил.\n\n"
                         "<b>▶️Узнайте больше о зонах отдыха в частном доме в кнопке «Подробнее»</b>\n\n"
                         "<b>Пожалуйста, отметьте, какие объекты планируете в своей зоне отдыха и релакса:</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)
    messages = cache37.get(message.chat.id, [])
    for msg in messages:
        bot.delete_message(message.chat.id, msg.message_id)


    





        
    
    


