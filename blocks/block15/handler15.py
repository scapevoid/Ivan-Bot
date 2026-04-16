from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove
from telebot.types import InputFile
from telebot.types import CallbackQuery

import asyncio





def block4_9(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    panoramic = InlineKeyboardButton("Панорамные окна", callback_data="panoramic")
    second_light = InlineKeyboardButton("Второй свет", callback_data="second_light")
    patio = InlineKeyboardButton("Плоская кровля с зоной отдыха", callback_data="patio")
    bay_window = InlineKeyboardButton("Эркер", callback_data="bay_window")
    atrium = InlineKeyboardButton("Атриум", callback_data="atrium")
    balcony = InlineKeyboardButton("Балкон", callback_data="balcony")
    basement = InlineKeyboardButton("Подвал", callback_data="basement")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_16")
    markup.add(panoramic, second_light, patio, bay_window, atrium, balcony, basement, continue_btw)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Красиво, атмосферно, а что ещё?</b>\n\n"
        "Рассказали про самые популярные архитектурные детали с точки зрения пользы для владельца.\n\n"
        "Именно эти элементы заказчики IVAN DOM чаще всего добавляют в проекты своих домов\n\n"
        "<b>Нажмите на кнопки, чтобы получить больше информации</b>\n\n",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)

        
    
    


