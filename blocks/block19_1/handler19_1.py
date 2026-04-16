from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery, InputFile

import asyncio





def block4_9(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_18")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_191")

    markup.add(InlineKeyboardButton("Металлочерепица", callback_data="variant_data_0__191"))
    markup.add(InlineKeyboardButton("Цементно-песчаная черепица", callback_data="variant_data_1__191"))
    markup.add(InlineKeyboardButton("Керамика", callback_data="variant_data_2__191"))
    markup.add(InlineKeyboardButton("Гибкая битумная черепица", callback_data="variant_data_3__191"))
    markup.add(InlineKeyboardButton("Композитная черепица", callback_data="variant_data_4__191"))
    markup.add(InlineKeyboardButton("Фальцевая кровля", callback_data="variant_data_5__191"))
    markup.add(InlineKeyboardButton("Плоская неэксплуатируемая кровля", callback_data="variant_data_6__191"))
    markup.add(InlineKeyboardButton("Плоская эксплуатируемая кровля", callback_data="variant_data_7__191"))
    markup.add(InlineKeyboardButton("Определим с архитектором", callback_data="skip_19_1"))
    markup.add(InlineKeyboardButton("ℹ️Подробнее", callback_data="podrobnee4"))


    markup.add(continue_btw, back)
    a = bot.send_photo(message.chat.id, InputFile("blocks/block19_1/crovla.jpg"),"<b>🔵 Как вы видите кровлю своего дома?</b>\n\n"
                         "<b>▶️Узнайте больше о видах кровли в кнопке «Подробнее»</b>\n\n"
                         "<i>Ваше решение может быть не окончательным – мы ещё обсудим его вместе с командой.</i>\n\n"
                         "<b>Пожалуйста, отметьте пункты, которые выбираете для кровли своего дома (их может быть несколько):</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)
        
    
    


