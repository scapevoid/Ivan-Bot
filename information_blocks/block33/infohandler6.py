import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
cache = {}
def infoblock9_0(message, bot):

    media = [
        InputMediaPhoto(open('information_blocks/block33/1.jpeg', 'rb')),
        InputMediaPhoto(open('information_blocks/block33/2.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block33/3.jpg', 'rb')),
        InputMediaPhoto(open('information_blocks/block33/4.jpg', 'rb')),
    ]
    data = bot.send_media_group(message.chat.id, media)
    cache[message.chat.id] = data

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("◀️ Назад", callback_data="continue_33333"),
    )
    bot.send_message(
        chat_id=message.chat.id,
        text='<b>🔵Детская — больше чем просто комната</b>\n\n'
                'Это личное пространство, где рождаются мечты, крепнет самостоятельность и расцветает индивидуальность.\n'
                'Для малышей важен уютный и безопасный мир с игровыми зонами и мягкими уголками.\n'
                'Школьникам требуется эргономичное рабочее место и системы хранения, чтобы учёба стала удобнее.\n'
                'Подростки оценят стильный и функциональный дизайн, где будет комфортно отдыхать, творить и принимать друзей. Используем экологичные материалы, умные решения и яркие детали, чтобы комната «росла» вместе с вашим ребёнком.\n\n'
                '<i>Благодаря детальному проекту мы создадим в доме идеальное пространство для каждого возраста.</i>',
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)