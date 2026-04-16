from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from telebot.types import InputFile


def block4_21(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_215")

    # определение данных 
    # [0] = определение что нужно сделать (выбрать)
    # [1] = дата -- которая хранится в text: str,
    # [2] = true or false 
    # [3] = данные о хандлере 
    # определение данных

    # если там сука выйдет ошибка тогда делаем на обычном тексте)))
    markup.add(InlineKeyboardButton("Прихожая", callback_data="prihojaya"))
    markup.add(InlineKeyboardButton("Гардеробная", callback_data="garderobnaya"))
    markup.add(InlineKeyboardButton("Санузел", callback_data="sanuzel"))
    markup.add(InlineKeyboardButton("Лапомойка", callback_data="lapomoyka"))



    markup.add(continue_btw)
    a = bot.send_message(
        message.chat.id,
        "<b>🔵Удобно с первых шагов</b>\n\n"
        "Входная зона или зона прихожей – первое впечатление о доме.\n\n"
        "<b>Узнайте больше о функциях и возможностях помещений этой части дома, чтобы грамотно спланировать пространство:</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)



    





        
    
    


