import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

def infoblock10_5(message, bot):

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Продолжить ▶️", callback_data="continue_143"),
    )
    bot.send_photo(
        chat_id=message.chat.id,
        photo=telebot.types.InputFile("information_blocks/block14_3/11.jpg"),
        caption='<b>🔵 Мы почти у цели!</b>\n\n'
                'На связи <b>Евгения Хошенко</b>, руководитель службы клиентской заботы IVAN DOM🤝\n\n'
                'Анкета на проектирование вашего дома готова на 90%.\n\n'
                'Как говорится у нас в IVAN DOM, семь раз отмерь, один раз – заполни анкету!\n\n'
                '<i>Ещё пару вопросов о целях – и анкета отправится в наш проектно-сметный отдел.</i>',
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)