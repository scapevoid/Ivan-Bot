from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()

from ..block27 import handler27
from ..block25 import handler25
from information_blocks.block26 import infohandler6
from ..block27.handler27 import cache as cache27
import createdb
def loads(message, bot, aaaa):
    if message.text == "Примеры гостиных":
        infohandler6.infoblock9_0(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    if message.text == "▶️ Пропустить":
        createdb.exdb("NULL", 30, message.chat.id)
        handler27.block4_27(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    if message.text == "◀️ Назад":
        handler25.block4_25(message, bot)
        bot.delete_message(message.chat.id, aaaa)
        return
    bot.delete_message(message.chat.id, aaaa)
    createdb.exdb(message.text, 30, message.chat.id)
    handler27.block4_27(message, bot)
    

def block4_26(message: Message, bot):
    back = KeyboardButton("Примеры гостиных")
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    continue_btw = KeyboardButton("▶️ Пропустить")
    nazad = KeyboardButton("◀️ Назад")
    markup.add(back)
    markup.add(continue_btw, nazad)
    a = bot.send_message(
        message.chat.id,
        "🔵 <b>Пожалуйста, в ответном сообщении расскажите нам о своих пожеланиях к центральной зоне дома</b>\n\n"
        "<i>Если дополнительных идей пока нет или вы хотели бы обсудить этот пункт на личной встрече с нашей командой – пожалуйста, пропустите этот вопрос.</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
    messages = cache27.get(message.chat.id, [])
    for msg in messages:
        bot.delete_message(message.chat.id, msg.message_id)
    
    


