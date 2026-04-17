import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
cache = {}
def infoblock9_0(message, bot):

    media = [
        InputMediaPhoto(open('information_blocks/block51/1.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block51/2.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block51/3.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block51/4.png', 'rb')),
    ]
    data = bot.send_media_group(message.chat.id, media)
    cache[message.chat.id] = data

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("◀️ Назад", callback_data="continue_513333"),
    )
    bot.send_message(
        chat_id=message.chat.id,
        text='<b>🔵 Залог хорошо налаженного быта в доме – продуманные и функциональные хозяйственные зоны</b>\n\n'
                'Это пространства для хранения необходимых предметов, бытовой техники, бытовых приспособлений и вещей, которые требуются лишь периодически.\n\n'
                'Грамотно спланированное размещение подсобных помещений, кладовых, прачечных и технических комнат значительно упрощает быт.\n\n'
                '<i>Владельцы дома высвобождают массу времени для занятий действительно важными и приятными вещами!</i>',
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)