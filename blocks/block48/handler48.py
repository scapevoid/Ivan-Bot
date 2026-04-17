from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery
from telebot.types import InputFile




def block4_46(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_475")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_48")
    markup.add(InlineKeyboardButton("Прачечная", callback_data="variant_data_0__48"))
    markup.add(InlineKeyboardButton("Кладовая", callback_data="variant_data_1__48"))
    markup.add(InlineKeyboardButton("Серверная", callback_data="variant_data_2__48"))
    markup.add(InlineKeyboardButton("Комната для персонала", callback_data="variant_data_3__48"))
    markup.add(InlineKeyboardButton("Инженерная", callback_data="variant_data_4__48"))
    markup.add(InlineKeyboardButton("Котельная", callback_data="variant_data_5__48"))
    markup.add(InlineKeyboardButton("Хозблок", callback_data="variant_data_6__48"))





    markup.add(continue_btw, back)
    a = bot.send_photo(
        message.chat.id, InputFile("blocks/block48/hz.jpg"),
        "<b>🔵Обсудим хозяйственную зону</b>\n\n"
        '<i>Какие помещения вы планируете, чтобы добавить своему дому практичности и удобства в быту?\n\n</i>'
        '<b>Пожалуйста, отметьте все необходимые пункты:</b>',
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)



    





        
    
    


