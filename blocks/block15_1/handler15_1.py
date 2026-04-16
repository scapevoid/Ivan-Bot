from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery, InputFile

import asyncio





def block15_1(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)


    back = InlineKeyboardButton("◀️ Назад", callback_data="return_14")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_151")

    markup.add(InlineKeyboardButton("Панорамные окна", callback_data="variant_data_0__151"))
    markup.add(InlineKeyboardButton("Второй свет", callback_data="variant_data_1__151"))
    markup.add(InlineKeyboardButton("Плоская кровля с зоной отдыха ", callback_data="variant_data_2__151"))
    markup.add(InlineKeyboardButton("Эркер", callback_data="variant_data_3__151"))
    markup.add(InlineKeyboardButton("Атриум", callback_data="variant_data_4__151"))
    markup.add(InlineKeyboardButton("Балкон", callback_data="variant_data_5__151"))
    markup.add(InlineKeyboardButton("Подвал", callback_data="variant_data_6__151"))
    markup.add(InlineKeyboardButton("Ничего из перечисленного", callback_data="nothing_first"))
    markup.add(InlineKeyboardButton("ℹ️Подробнее", callback_data="podrobnee2"))

    markup.add(continue_btw, back)
    a = bot.send_photo(
        message.chat.id, InputFile("blocks/block15_1/chidt.jpg"),
        "🔵 <b>Добавим вашему дому особенный характер!</b>\n\n"
        "Архитектурные детали создают неповторимый облик здания. А ещё каждый элемент влияет и на эстетику здания, и на уровень вашего комфорта.\n\n"
        "<b>▶️Узнайте больше об архитектурных деталях в кнопке «Подробнее»</b>\n\n"
        "<i>Ваше решение может быть не окончательным – мы ещё обсудим его вместе с командой.</i>\n\n"
        "<b>Пожалуйста, отметьте все архитектурные детали, что вы планируете в будущем доме, или пропустите вопрос</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)

        
    
    


