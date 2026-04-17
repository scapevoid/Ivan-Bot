from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
cache = {}
def infoblock9_0(message, bot):

    media = [
        InputMediaPhoto(open('information_blocks/block26/1.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block26/2.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block26/3.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block26/4.jpg', 'rb')),
    ]

    data = bot.send_media_group(message.chat.id, media)
    cache[message.chat.id] = data
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("◀️ Назад", callback_data="continue_26333"),
    )
    bot.send_message(
        chat_id=message.chat.id,
        text='<b>🔵Точка притяжения для всей семьи</b>\n\n'
                'Просторное и уютное пространство с идеальной планировкой создано для семейных вечеров, теплых встреч друзей и ярких торжеств.\n'
                'Это «место для всех», поэтому так важно спроектировать гостиную удобно и функционально.\n'
                'Можно объединить её с зонами столовой и кухни, чтобы максимально открыть пространство и наполнить дом простором.\n'
                'Или сделать гостиную и кухню автономными, сохраняя максимум эстетики парадным помещениям дома.\n'
                'Примыкающая к гостиной терраса эффектно увеличит пространство и наполнит его светом и воздухом.\n\n'
                '<i>Спроектируем главную точку притяжения в вашем доме по вашим правилам и придадим гостиной ваш характер!</i>',
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)