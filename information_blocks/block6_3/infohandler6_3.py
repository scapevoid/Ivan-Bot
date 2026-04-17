import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

def infoblock6_3(message, bot):
    
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Продолжить ▶️", callback_data="continue_63"),
    )
    bot.send_photo(
        chat_id=message.chat.id,
        photo=telebot.types.InputFile("information_blocks/block6_3/6_3.jpg"),
        caption='<b>🔵 Ваша продуктивность заслуживает похвал!</b>\n\n'
                'На связи <b>Татьяна Михайлова</b>, руководитель отдела проектирования IVAN DOM Rostov\n\n'
                'Чтобы соответствовать такой целеустремлённости, будем ещё тщательнее следить за графиками👌🏻\n\n'
                '<b>Ждём заполненную анкету, мы на низком старте!</b>',
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.delete_message(message.chat.id, message.id)