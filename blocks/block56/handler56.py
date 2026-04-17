from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery




def block4_56(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_55")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_56")
    markup.add(InlineKeyboardButton("Геометричность", callback_data="variant_data_0__56"))
    markup.add(InlineKeyboardButton("Естественность", callback_data="variant_data_1__56"))
    markup.add(InlineKeyboardButton("Минимализм", callback_data="variant_data_2__56"))
    markup.add(InlineKeyboardButton("Много зелени", callback_data="variant_data_3__56"))
    markup.add(InlineKeyboardButton("Функционал важнее стиля", callback_data="variant_data_4__56"))
    markup.add(InlineKeyboardButton("ℹ️Подробнее", callback_data="podrobnee9"))
    





    markup.add(continue_btw, back)
    a = bot.send_message(message.chat.id, "<b>🔵Ландшафтный дизайн</b>\n\n"
                         "Спланируйте неповторимый ландшафт своего участка в гармонии со своими вкусами, обликом дома и окружающей природы. Это сделает эстетику всего домовладения завершённой и отразит ваше личное понимание прекрасного.\n\n"
                         "<b>▶️Узнайте больше о разных стилях ландшафтного дизайна в кнопке «Подробнее»</b>\n\n"
                         "<b>Пожалуйста, отметьте, какой стиль ландшафтного дизайна вам ближе:</b>",
                         parse_mode="HTML",
                         reply_markup=markup)
    bot.delete_message(message.chat.id, message.id)


    





        
    
    


