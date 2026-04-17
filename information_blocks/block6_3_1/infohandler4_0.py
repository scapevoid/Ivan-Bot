import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

def infoblock6_3(message, bot):
    
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Продолжить ▶️", callback_data="continue_41111"),
    )
    bot.send_photo(
        chat_id=message.chat.id,
        photo=telebot.types.InputFile("information_blocks/block6_3_1/4_0.jpg"),
        caption='<b>🔵На связи Дмитрий Любченко, ведущий архитектор IVAN DOM</b>\n\n'
                'По графику самое время обсудить важные детали будущего дома.\n\n'
                '<i>Площадь, этажность, архитектура – пришла пора поговорить про действительно важные вещи! Готовы?</i>',
        parse_mode='HTML',
        reply_markup=markup
    )
    try:
        bot.delete_message(message.chat.id, message.id-1)
    except Exception as e:
        pass
    try:
        bot.delete_message(message.chat.id, message.id)
    except Exception as e:
        pass