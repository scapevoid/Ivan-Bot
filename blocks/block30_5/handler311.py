from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery




def block4_31(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_31")

    markup.add(InlineKeyboardButton("Игровая комната", callback_data="asdfasdfadffdsfsadfsadf"))
    markup.add(InlineKeyboardButton("Комната для занятий", callback_data="asdfasdfasdfasdf"))
    markup.add(InlineKeyboardButton("Гардеробная", callback_data="asdfasdfasdsadasdfff"))
    markup.add(InlineKeyboardButton("Детский санузел", callback_data="asdfasdfsadfasdf1"))



    markup.add(continue_btw)
    a = bot.send_message(
        message.chat.id,
        "<b>🔵Ещё милые малыши или уже колючие подростки?</b>\n\n"
        "<i>Иметь свою личную территорию важно для любого возраста.\nИ это не про баловство, а про мощный старт, что так помогает в жизненной гонке.</i>\n\n"
        "<b>Узнайте подробнее, какие возможности есть у современных детских:</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)


    





        
    
    


