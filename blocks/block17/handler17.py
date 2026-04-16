from telebot import TeleBot
from telebot.types import Message
from telebot.types import InputFile
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

import asyncio





def block4_9(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    panoramic = InlineKeyboardButton("Кирпич керамический", callback_data="ceramic_brick")
    second_light = InlineKeyboardButton("Кирпич ручной формовки", callback_data="handmade_brick")
    patio = InlineKeyboardButton("Ригель ручной формовки", callback_data="handmade_riegel")
    flat_roof = InlineKeyboardButton("Декоративная штукатурка", callback_data="decorative_plaster")
    bay_window = InlineKeyboardButton("Натуральное дерево", callback_data="natural_wood")
    atrium = InlineKeyboardButton("Природный камень", callback_data="natural_stone")
    balcony = InlineKeyboardButton("Фасадные панели", callback_data="facade_panels")
    basement = InlineKeyboardButton("Гибкая керамика", callback_data="flexible_ceramics")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_18")
    markup.add(panoramic, second_light, patio, flat_roof, bay_window, atrium, balcony, basement, continue_btw)
    a = bot.send_message(
        message.chat.id,
        "<b>🔵Секреты фасадных материалов</b>\n\n"
        "От выбора фасадных материалов зависит внешняя эстетика дома, его долговечность и энергоэффективность.\n\n"
        "<b>Вот информация про материалы для внешней отделки дома, полпулярные у наших заказчиков:</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)