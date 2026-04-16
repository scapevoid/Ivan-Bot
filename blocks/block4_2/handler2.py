from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

import time
from telebot.types import CallbackQuery
import getpath
from ..block4_3 import handler3
from ..block4_1 import handler1

path = getpath.pathreturn()
import createdb
def loads(message, bot, idaa):
    # read = open(f"{path}{message.chat.id}_id", "r", encoding="UTF-8")
    # file = open(f"{path}{message.chat.id}_id", "a", encoding="UTF-8")
    # data = read.readline()

    if message.text == "◀️ Назад":
        handler1.block4_1(message, bot)
        bot.delete_message(message.chat.id, idaa)
        return


    if not (hasattr(message, "text") and message.text and all(x.isalpha() or x.isspace() for x in message.text)):
        a = bot.send_message(message.chat.id, "Отправьте корректные данные")
        time.sleep(3)
        bot.delete_message(message.chat.id, a.id)
        bot.delete_message(message.chat.id, idaa)
        block4_2(message, bot)
        return
    bot.delete_message(message.chat.id, idaa)
    createdb.exdb(message.text, 2, message.chat.id)
    handler3.block4_3(message, bot)
    

def block4_2(message: Message, bot):
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    nazad = KeyboardButton("◀️ Назад")
    markup.add(nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 Чтобы мы зафиксировали ваши ответы в персональном файле:\n\n"
        "<b>Пожалуйста, в ответном сообщении напишите ваше имя и фамилию.</b>\n\n"
        "<i>Мы не передаем персонализированную информацию о своих клиентов третьим лицам.</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler_by_chat_id(message.chat.id, lambda msg: loads(msg, bot, a.id))
    try:
        bot.delete_message(message.chat.id, message.id)
    except Exception:
        print("start error" + str(message.chat.id))
        pass
        
    
    


