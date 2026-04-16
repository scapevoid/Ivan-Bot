from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block17_1 import handler17_1
from ..block15_1 import handler15_1
import getpath
import createdb

path = getpath.pathreturn()

import requests


def loads(message, bot, aaaa):
    if message.text == "▶️ Пропустить":
        createdb.exdb("NULL", 18, message.chat.id)
        bot.delete_message(message.chat.id, aaaa)
        handler17_1.block17_1(message, bot)
        return
    if message.text == "◀️ Назад":
        handler15_1.block15_1(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    if hasattr(message, 'photo') and message.photo:
        url_img = bot.get_file_url(message.photo[-1].file_id)

        params = {
            "key": "7efdddd1053b6c6489b20e7e8e73a551",
            "expiration": 600,
        }
        files = {
            "image": (None, url_img)
        }
        data = requests.post(url=r"https://api.imgbb.com/1/upload", params=params, files=files).json()
        if data.get("success") and "data" in data and "url" in data["data"]:
            if message.caption:
                message.text = (message.caption or "") +"  "+ data["data"]["url"]
            else:
                message.text = data["data"]["url"]
        print(message.text)
    createdb.exdb(message.text, 18, message.chat.id)
    bot.delete_message(message.chat.id, aaaa)
    handler17_1.block17_1(message, bot)
    

def block4_11(message: Message, bot):
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    continue_btw = KeyboardButton("▶️ Пропустить")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(continue_btw, nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожалуйста, в ответном сообщении расскажите о других деталях будущего дома.</b>\n\n"
        "<i>Фото и скрины деталей, которые вас вдохновляют, помогают нам лучше понять ваши вкусы и ожидания. Их также можно прикрепить к сообщению.</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
    
    


