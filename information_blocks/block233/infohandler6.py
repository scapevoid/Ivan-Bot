import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
cache = {}

def infoblock9_0(message, bot):

    media = [
        InputMediaPhoto(open('information_blocks/block233/1.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block233/2.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block233/3.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block233/4.jpg', 'rb'))
    ]
    data = bot.send_media_group(message.chat.id, media)
    cache[message.chat.id] = data
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("◀️ Назад", callback_data="continue_23333"),
    )
    bot.send_message(
        chat_id=message.chat.id,
        text='🔵 <b>Первое впечатление — самое важное</b>\n\n'
                '<i>Функциональная и продуманная велком-зона задаст тон всему остальному пространству дома.</i>',
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)