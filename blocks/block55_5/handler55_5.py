from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery




def block4_56(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_575")
    markup.add(InlineKeyboardButton("Геометричность", callback_data="geomet"))
    markup.add(InlineKeyboardButton("Естественность", callback_data="ecetest"))
    markup.add(InlineKeyboardButton("Минимализм", callback_data="minimalizmastion"))
    markup.add(InlineKeyboardButton("Много зелени", callback_data="mnogazeleni"))
    markup.add(InlineKeyboardButton("Функционал важнее стиля", callback_data="functional"))
    





    markup.add(continue_btw)
    a = bot.send_message(message.chat.id, "<b>🔵В гармонии с природой</b>\n\n"
                         "Дизайн участка так же важен, как и отделка дома. Именно так домовладение приобретает завершённый вид, а вы выражаете свои предпочтения и характер.\n\n"
                         "<b>Узнайте подробнее о разных ландшафтных стилях, чтобы найти свой:</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)


    





        
    
    


