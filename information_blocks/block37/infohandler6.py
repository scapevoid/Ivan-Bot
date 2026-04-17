import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
cache = {}
def infoblock9_0(message, bot):

    media = [
        InputMediaPhoto(open('information_blocks/block37/1.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block37/2.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block37/3.png', 'rb')),
        InputMediaPhoto(open('information_blocks/block37/4.jpg', 'rb')),
    ]
    data = bot.send_media_group(message.chat.id, media)
    cache[message.chat.id] = data

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("◀️ Назад", callback_data="continue_333333"),
    )
    bot.send_message(
        chat_id=message.chat.id,
        text='<b>🔵Оптимальное число санузлов в доме зависит от образа жизни владельцев</b>\n\n'
                'Тщательно выверенное количество душевых, туалетных комнат и помещений для гостей – это про удобство владельцев дома и гостей.\n'
                'Это действительно важный вопрос, который важно продумать на этапе проектирования.\n\n'
                '<i>Благодаря детальному проекту мы создадим в доме идеальное пространство для каждого возраста.</i>',
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)