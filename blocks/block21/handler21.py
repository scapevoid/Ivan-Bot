from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery, InputFile




def block4_21(message: Message, bot):
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="return_20")
    continue_btw = InlineKeyboardButton("Продолжить ▶️", callback_data="continue_21")
    markup.add(InlineKeyboardButton("Прихожая", callback_data="variant_data_0__21"))
    markup.add(InlineKeyboardButton("Гардеробная", callback_data="variant_data_1__21"))
    markup.add(InlineKeyboardButton("Санузел", callback_data="variant_data_2__21"))
    markup.add(InlineKeyboardButton("Лапомойка", callback_data="variant_data_3__21"))
    markup.add(InlineKeyboardButton("ℹ️Подробнее", callback_data="podrobnee5"))



    markup.add(continue_btw, back)
    a = bot.send_photo(
        message.chat.id,InputFile("blocks/block21/funkom.jpg"),
        "<b>🔵Определяем функционал комнат</b>\n\n"
        "Мы разделили дом на зоны с разными задачами и целями, чтобы сделать пространство уютным, эргономичным и максимально «вашим».\n\n"
        "<b>И первой мы обсудим входную зону.</b>\n\n"
        "<b>▶️Узнайте больше о помещениях в этой зоне в кнопке «Подробнее»</b>\n\n"
        "<b>Пожалуйста, отметьте все помещения, нужные вам во входной зоне будущего дома:</b>",
        parse_mode="HTML",
        reply_markup=markup
    )
    try:
        bot.delete_message(message.chat.id, message.id)
    except Exception:
        pass



    





        
    
    


