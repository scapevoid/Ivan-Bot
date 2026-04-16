from telebot import TeleBot
from telebot.types import Message
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputFile

from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove
from telebot.types import CallbackQuery

import asyncio




def block4_9(message: Message, bot):

    markup = InlineKeyboardMarkup(row_width=1)
    biznes = InlineKeyboardButton("Бизнес-класс", callback_data="biznes")
    comfort = InlineKeyboardButton("Комфорт-класс", callback_data="comfort")
    premium = InlineKeyboardButton("Премиум-класс", callback_data="premium")
    continue_btn = InlineKeyboardButton("Продолжить ▶️", callback_data="goto4_10")
    markup.add(comfort, biznes, premium, continue_btn)
    a = bot.send_message(
        message.chat.id,
        "<b>🔵Класс комфорта: что это и зачем нужно?</b>\n\n"
        "Мы в IVAN DOM Rostov строим дома трёх категорий. Они различаются комфортностью проживания, долговечностью конструкций, ценовыми категориями стройматериалов и уровнем технической сложности инженерных решений\n\n"
        "При любом выбранном варианте вы получаете:\n"
        "🔹строительство в точности по проекту\n"
        "🔹прозрачность договорённостей\n"
        "🔹исчерпывающую информацию о материалах и проектных решениях\n"
        "🔹соблюдение сроков, условий и критериев качества\n\n"
        "Все эти пункты мы согласовываем с вами и фиксируем в договоре подряда.\n\n"
        "Как итог, ваши ожидания и результат строительства совпадают на 100%.\n\n"
        "<b>Чем конкретно отличаются дома разных категорий комфорта?</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)
        
    
    


