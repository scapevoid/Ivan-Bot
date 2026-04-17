from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton





def block4_34(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_44")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_455")
    
    markup.add(InlineKeyboardButton("Ванна", callback_data="variant_data_0__445"))
    markup.add(InlineKeyboardButton("Душ", callback_data="variant_data_1__445"))
    markup.add(InlineKeyboardButton("Тропический душ", callback_data="variant_data_2__445"))
    markup.add(InlineKeyboardButton("Раковина", callback_data="variant_data_3__445"))
    markup.add(InlineKeyboardButton("Двойная раковина", callback_data="variant_data_4__445"))
    markup.add(InlineKeyboardButton("Унитаз", callback_data="variant_data_5__445"))
    markup.add(InlineKeyboardButton("Биде", callback_data="variant_data_6__445"))
    markup.add(InlineKeyboardButton("Гигиенический душ", callback_data="variant_data_7__445"))




    markup.add(continue_btw, back)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Выберите наполнение санузла №4</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)



    





        
    
    


