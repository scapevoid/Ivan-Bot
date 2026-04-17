import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
cache5551 = {}
def infoblock10_5(message, bot):

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Продолжить ▶️", callback_data="continue_11221"))
    bot.send_photo(
        chat_id=message.chat.id,
        photo=telebot.types.InputFile("information_blocks/block11/11.jpg"),
        caption='<b>🔵 Обсудим параметры участка под строительство</b>\n\n'
                'Характеристики участка – база процесса проектирования. От них зависят многие проектные решения (например, тип фундамента), выбор конфигурации будущего дома, и, в итоге, стоимость строительства.\n\n'
                'Расскажите об участке максимально подробно, и мы предложим вам оптимальные проектные решения.\n\n'
                '<b>Если затрудняетесь указать какие-то параметры — мы поможем собрать недостающую информацию позже.</b>',
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)
    messages = cache5551.get(message.chat.id, [])
    for msg in messages:
        bot.delete_message(message.chat.id, msg.message_id)