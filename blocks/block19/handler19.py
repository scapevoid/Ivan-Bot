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
    metal_tile = InlineKeyboardButton("Металлочерепица", callback_data="metal_tile")
    cement_sand_tile = InlineKeyboardButton("Цементно-песчаная черепица", callback_data="cement_sand_tile")
    ceramic_tile = InlineKeyboardButton("Керамическая черепица", callback_data="ceramic_tile")
    bitumen_tile = InlineKeyboardButton("Гибкая битумная черепица", callback_data="bitumen_tile")
    composite_tile = InlineKeyboardButton("Композитная черепица", callback_data="composite_tile")
    seam_roof = InlineKeyboardButton("Фальцевая кровля", callback_data="seam_roof")
    flat_roof = InlineKeyboardButton("Плоская неэксплуатируемая кровля", callback_data="flat_roof")
    asdf = InlineKeyboardButton("Плоская эксплуатируемая", callback_data="notflat_roof")
    continue_btn = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_20")


    markup.add(metal_tile)
    markup.add(cement_sand_tile)
    markup.add(ceramic_tile)
    markup.add(bitumen_tile)
    markup.add(composite_tile)
    markup.add(seam_roof)
    markup.add(flat_roof)
    markup.add(asdf)
    markup.add(continue_btn)
    a = bot.send_message(
        message.chat.id,
        "<b>🔵Кровля: о чём полезно знать</b>\n\n"
        "Рады поделиться своими строительными знаниями ровно настолько, насколько это вам нужно и интересно.\n\n"
        "<b>Вот важные блоки информации по материалам и конфигурации кровель в частном доме:</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)
        
    
    


