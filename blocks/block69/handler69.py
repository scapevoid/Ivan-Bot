from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery




def block4_46(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_68")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_70")
    markup.add(InlineKeyboardButton("Снос строений", callback_data="variant_data_0__70"))
    markup.add(InlineKeyboardButton("Спил и корчевание деревьев", callback_data="variant_data_1__70"))
    markup.add(InlineKeyboardButton("Пересадка растений", callback_data="variant_data_2__70"))
    markup.add(InlineKeyboardButton("Уборка мусора", callback_data="variant_data_3__70"))
    markup.add(InlineKeyboardButton("Земляные работы", callback_data="variant_data_4__70"))
    markup.add(InlineKeyboardButton("Монтаж подпорных стенок", callback_data="variant_data_5__70"))
    markup.add(InlineKeyboardButton("Оградить участок", callback_data="variant_data_6__70"))
    markup.add(InlineKeyboardButton("Участок готов к стройке", callback_data="gotovkstroyke"))

    



    markup.add(continue_btw, back)
    a = bot.send_message(message.chat.id, "<b>🔵 Какие подготовительные работы необходимо провести на участке?</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)


    





        
    
    


