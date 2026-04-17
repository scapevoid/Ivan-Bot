import telebot
from telebot.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

def infoblock9_0(message, bot):
    bot.delete_message(message.chat.id, message.id)

    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Продолжить ▶️", callback_data="continue_90"),
    )
    bot.send_photo(
        chat_id=message.chat.id,
        photo=telebot.types.InputFile("information_blocks/block9/9.jpg"),
        caption='🔵 <b>Докладываю: идём чётко по графику!</b>\n\n'
                '<b>На связи Петр Геннадьевич, прораб IVAN DOM</b>\n\n'
                'Впереди у вас важный раздел анкеты про наполнение дома. Для будущего проекта эти сведения так же важны, как фундамент – для дома.\n\nОснова основ.\n\n'
                '<i>Если что, мы с командой рядом и готовы ответить на все ваши вопросы\n\nЖму вашу руку</i>',
        parse_mode="HTML",
        reply_markup=markup
    )