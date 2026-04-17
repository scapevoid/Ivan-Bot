import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

def infoblock6_3(message, bot):
    
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Продолжить ▶️", callback_data="continue_4111"),
    )
    bot.send_photo(
        chat_id=message.chat.id,
        photo=telebot.types.InputFile("information_blocks/block4/4_0.jpg"),
        caption='<b>🔵 Дом – это больше, чем просто стены</b>\n\n'
                'Это ваше качество жизни, ваша энергия, вдохновение и статус.\n\n'
                'Чтобы дом знал всё о ваших вкусах, привычках и образе жизни, для начала обсудим самое важное: ваши цели и ожидания от строительства.\n\n'
                '<b>Мы выразим ваши пожелания в доме, который будет радовать и наполнять вас. А еще сбалансируем ваши ожидания и бюджет.</b>',
        parse_mode='HTML',
        reply_markup=markup
    )
    try:
        bot.delete_message(message.chat.id, message.id)
    except Exception as e:
        pass