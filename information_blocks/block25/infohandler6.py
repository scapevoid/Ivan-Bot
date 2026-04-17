import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
cache = {}
def infoblock9_0(message, bot):

    media = [
        InputMediaPhoto(open('information_blocks/block25/1.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block25/2.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block25/3.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block25/4.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block25/5.jpg', 'rb'))
    ]
    data = bot.send_media_group(message.chat.id, media)
    cache[message.chat.id] = data
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("◀️ Назад", callback_data="continue_25333"),
    )
    bot.send_message(
        chat_id=message.chat.id,
        text='<b>🔵Терраса — связь с природой и дополнительная зона отдыха</b>\n\n'
                'Здесь можно разместить обеденную группу, шезлонги или даже летнюю кухню. Важно продумать защиту от солнца, ветра и выбрать долговечные материалы.\n\n'
                '<i>Вместе мы создадим террасу, где вы будете наслаждаться каждым моментом!</i>',
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)