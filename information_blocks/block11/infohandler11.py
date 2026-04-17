import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
cache5551 = {}
def infoblock10_5(message, bot):

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Продолжить ▶️", callback_data="continue_111"))
    markup.add(InlineKeyboardButton("Планировка участка", callback_data="planirivkauchastka"))
    bot.send_photo(
        chat_id=message.chat.id,
        photo=telebot.types.InputFile("information_blocks/block11/11.jpg"),
        caption='<b>🔵Организовываем пространство двора</b>\n\n'
                'Слияние с природой и жизнь вне городских рамок  – особая привилегия владельца частного дома. И даёт её, конечно, уютное ипродуманное пространство двора.\n\n'
                'Реализовывать все планы на него можно постепенно, а планировать – лучше сразу. Это поможет оптимизировать работу и расходы на благоустройство до 70%.\n\n',
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)
    messages = cache5551.get(message.chat.id, [])
    for msg in messages:
        bot.delete_message(message.chat.id, msg.message_id)