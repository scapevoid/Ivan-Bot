from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton





def block4_34(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_42")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_43")
    
    markup.add(InlineKeyboardButton("Ванна", callback_data="variant_data_0__43"))
    markup.add(InlineKeyboardButton("Душ", callback_data="variant_data_1__43"))
    markup.add(InlineKeyboardButton("Тропический душ", callback_data="variant_data_2__43"))
    markup.add(InlineKeyboardButton("Раковина", callback_data="variant_data_3__43"))
    markup.add(InlineKeyboardButton("Двойная раковина", callback_data="variant_data_4__43"))
    markup.add(InlineKeyboardButton("Унитаз", callback_data="variant_data_5__43"))
    markup.add(InlineKeyboardButton("Биде", callback_data="variant_data_6__43"))
    markup.add(InlineKeyboardButton("Гигиенический душ", callback_data="variant_data_7__43"))




    markup.add(continue_btw, back)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Выберите наполнение санузла №3</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)



    





        
    
    


