from telebot import TeleBot
from telebot.types import Message

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import ReplyKeyboardRemove

from telebot.types import CallbackQuery

from ..block21 import handler21
import getpath

path = getpath.pathreturn()
from ..block75.handler75 import cache as cache33
from ..block75 import handler75
from ..block77 import handler77
import createdb
from ..block4_1 import handler1
def loads(message, bot, aa):
    if message.text == "◀️ Назад":
        handler75.block4_40(message, bot)
        bot.delete_message(message.chat.id, aa)
        return
    if message.text == "Продолжить ▶️":
        handler77.block4_40(message, bot)
        bot.delete_message(message.chat.id, aa)
        return
    if message.text == "Заполнить анкету заново":
        handler1.block4_1(message, bot)
        bot.delete_message(message.chat.id, aa)
        return
    bot.delete_message(message.chat.id, aa)
    createdb.exdb(message.text, 88, message.chat.id)
    handler77.block4_40(message, bot)
    

def block4_40(message: Message, bot):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(KeyboardButton("Заполнить анкету заново"))
    markup.add(KeyboardButton("Продолжить ▶️"))
    markup.add(KeyboardButton("◀️ Назад"))

    a = bot.send_message(
        message.chat.id,
        "<b>🔵  Давайте уточним!</b>\n\n"
        "Если мы не обсудили какой-то важный момент, касающийся вашего будущего дома – пожалуйста, напишите нам о своих идеях, пожеланиях, параметрах  в ответном сообщении.\n\n"
        "<b>Если вы хотите изменить свои ответы или обсудить их с близкими – пожалуйста, заполните анкету ещё раз.</b>\n\n"
        "<i>Если в каком-то разделе у вас пока нет чёткого видения своих пожеланий, или у вас возникли вопросы по будущему проекту дома – мы всегда на связи!</i>",
        parse_mode="HTML",
        reply_markup=markup
    )
    bot.register_next_step_handler(a, lambda msg: loads(msg, bot, a.id))
    bot.delete_message(message.chat.id, message.id)
    messages = cache33.get(message.chat.id, [])
    for msg in messages:
        bot.delete_message(message.chat.id, msg.message_id)
    
    


