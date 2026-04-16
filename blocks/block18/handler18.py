from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery


from ..block19_1 import handler19_1
from ..block17_1 import handler17_1
import getpath

path = getpath.pathreturn()
import createdb



def loads(message, bot, aaaa):
    if message.text == "▶️ Пропустить":
        createdb.exdb("NULL", 20, message.chat.id)

        handler19_1.block4_9(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    if message.text == "◀️ Назад":
        handler17_1.block17_1(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    bot.delete_message(message.chat.id, aaaa)
    createdb.exdb(message.text, 20, message.chat.id)
    handler19_1.block4_9(message, bot)
    

def block4_11(message: Message, bot):
    
    markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    continue_btw = KeyboardButton("▶️ Пропустить")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(continue_btw, nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожалуйста, в ответном сообщении расскажите нам об особых пожеланиях к отделке фасадов.</b>\n\n"
        "<i>Если дополнительных идей пока нет или вы хотели бы обсудить этот пункт на личной встрече с нашей командой – пожалуйста, пропустите этот вопрос.</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
    
    


