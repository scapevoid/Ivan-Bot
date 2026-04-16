from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery, InputFile

import asyncio





def block17_1(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_16")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_171")

    markup.add(InlineKeyboardButton("Кирпич керамический", callback_data="variant_data_0__171"))
    markup.add(InlineKeyboardButton("Кирпич ручной формовки", callback_data="variant_data_1__171"))
    markup.add(InlineKeyboardButton("Ригель ручной формовки", callback_data="variant_data_2__171"))
    markup.add(InlineKeyboardButton("Декоративная штукатурка", callback_data="variant_data_3__171"))
    markup.add(InlineKeyboardButton("Натуральное дерево", callback_data="variant_data_4__171"))
    markup.add(InlineKeyboardButton("Природный камень", callback_data="variant_data_5__171"))
    markup.add(InlineKeyboardButton("Фасадные панели", callback_data="variant_data_6__171"))
    markup.add(InlineKeyboardButton("Гибкая керамика", callback_data="variant_data_7__171"))
    markup.add(InlineKeyboardButton("ℹ️Подробнее", callback_data="podrobnee3"))

    markup.add(continue_btw, back)
    a = bot.send_photo(
        message.chat.id, InputFile("blocks/block17_1/fasadd.jpg"),
        "<b>🔵Выбор фасадных материалов</b>\n\n"
        "Нам важно подобрать оптимальный вариант, подходящий стилю архитектуры, климатическим условиям региона и вашему бюджету.\n\n"
        "<b>▶️Узнайте больше о фасадных материалах в кнопке «Подробнее»</b>\n\n"
        "<i>Ваше решение может быть не окончательным – мы ещё обсудим его вместе с командой.</i>\n\n"
        "<b>Пожалуйста, выберите материалы для отделки фасадов вашего дома:</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)
