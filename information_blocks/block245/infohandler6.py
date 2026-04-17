import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
cache = {}
def infoblock9_0(message, bot):

    media = [
        InputMediaPhoto(open('information_blocks/block245/1.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block245/2.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block245/3.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block245/4.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block245/5.jpg', 'rb'))
    ]
    data = bot.send_media_group(message.chat.id, media)
    cache[message.chat.id] = data
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("◀️ Назад", callback_data="continue_24333"),
    )
    bot.send_message(
        chat_id=message.chat.id,
        text='<b>🔵Если дом – это государство, то кухня – его кулинарная столица.</b>\n\n'
                'Важно продумать эргономику рабочего треугольника, систематизировать хранение и использовать лишь надёжные решения.\n\n'
                '<i>Остров или барная стойка, максимум функционала или минимализм — давайте сделаем кухню вашей мечты, где даже заварить чай станет ритуалом удовольствия.</i>',
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)