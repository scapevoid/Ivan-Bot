import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

def infoblock10_5(message, bot):
    

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Продолжить ▶️", callback_data="continue_110"),
    )
    bot.send_photo(
        chat_id=message.chat.id,
        photo=telebot.types.InputFile("information_blocks/block10_5/10_5.jpg"),
        caption='🔵 <b>Идём на рекорд!</b>\n\n'
                'Мы в IVAN DOM сдаём 100% наших объектов точно в срок по договору или даже раньше. Кажется, в заполнении анкеты вы придерживаетесь такой же тактики🤝🏻\n\n'
                'Соберём последние детали и обсудим  сроки и точную стоимость вашего будущего проекта.\n\n'
                '<b>Вы  почти у цели!</b>',
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)
