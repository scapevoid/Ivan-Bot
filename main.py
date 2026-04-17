from telebot import TeleBot
from telebot.types import Message, CallbackQuery
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InputFile, InputMediaPhoto
import createdb
import gettokenbot
# это вопросы
from blocks.block38_3 import handler38_3
from blocks.block42_3 import handler42_3
from blocks.block38_2 import handler38_2
from blocks.block40_2 import handler402
from blocks.block4_1 import handler1
from blocks.block4_3 import handler3
from blocks.block4_4 import handler4
from blocks.block4_5 import handler5
from blocks.block4_5_1 import handler6 as handler451
from blocks.block4_6 import handler4_6
from blocks.block6 import handler6
from blocks.block4_5_1 import handler6 as handler600
from blocks.block8 import handler8
from blocks.block9 import handler9
from blocks.block10 import handler10
from blocks.block11 import handler11
from blocks.block12 import handler12
from blocks.block12_1 import handler12_1
from blocks.block13_1 import handler13_1 
from blocks.block15_1 import handler15_1
from blocks.block17_1 import handler17_1
from blocks.block19_1 import handler19_1
from blocks.block20_5 import handler20_5
from blocks.block22_1 import handler233
from blocks.block51_5 import handler51_5
from blocks.block45_5 import handler45_5
from blocks.block53_5 import handler53_5
from blocks.block54_5 import handler54_5
from blocks.block55_5 import handler55_5
from blocks.block73_1 import handler73_1
from blocks.block73_5 import handler73_5
from blocks.block13 import handler13
from blocks.block14 import handler14
from blocks.block15 import handler15
from blocks.block16 import handler16
from blocks.block17 import handler17
from blocks.block18 import handler18
from blocks.block19 import handler19
from blocks.block20 import handler20
from blocks.block21 import handler21
from blocks.block22 import handler22
from blocks.block23 import handler23
from blocks.block24 import handler24
from blocks.block24_5 import handler24_5
from blocks.block25 import handler25
from blocks.block26 import handler26
from blocks.block27 import handler27
from blocks.block28 import handler28
from blocks.block29 import handler29
from blocks.block30 import handler30
from blocks.block30_5 import handler311
from blocks.block31 import handler31
from blocks.block32 import handler32
from blocks.block33 import handler33
from blocks.block34 import handler34
from blocks.block35 import handler35
from blocks.block36 import handler36
from blocks.block37 import handler37
from blocks.block38 import handler38
from blocks.block40 import handler40
from blocks.block42 import handler42
from blocks.block44 import handler44 
from blocks.block45 import handler45
from blocks.block46 import handler46
from blocks.block49 import handler49
from blocks.block47 import handler47
from blocks.block47_5 import handler47_5
from blocks.block51 import handler51
from blocks.block52 import handler52
from blocks.block53 import handler53
from blocks.block53_4 import handler53_4
from blocks.block54_5 import handler54_5
from blocks.block73_1 import handler73_1
from blocks.block53_1 import handler54_1
from blocks.block54 import handler54
from blocks.block55 import handler55
from blocks.block56 import handler56
from blocks.block57 import handler57
from blocks.block58 import handler58
from blocks.block59 import handler59
from blocks.block61 import handler61
from blocks.block62 import handler62
from blocks.block63 import handler63
from blocks.block64 import handler64
from blocks.block65 import handler65
from blocks.block66 import handler66
from blocks.block67 import handler67
from blocks.block69 import handler69
from blocks.block71 import handler71
from blocks.block70 import handler711
from blocks.block72 import handler72
from blocks.block73 import handler73
from blocks.block74 import handler74
from blocks.block75 import handler75
from blocks.block76 import handler76
from blocks.block68_5 import handler68_5
from blocks.block76.handler76 import block4_40
import zipfile

# это информационные блоки
from information_blocks.block233.infohandler6 import cache as cache233
from information_blocks.block245.infohandler6 import cache as cache245
from information_blocks.block25.infohandler6 import cache as cache25
from information_blocks.block33.infohandler6 import cache as cache33
from information_blocks.block37.infohandler6 import cache as cache37
from information_blocks.block51.infohandler6 import cache as cache51
from blocks.block75.handler75 import cache as cache75
from blocks.block74.handler74 import cache as cache74
from blocks.block73_5.handler73_5 import cache as cache735
from information_blocks.block11.infohandler11 import cache5551
from blocks.block73.handler73 import cache as cache73
from blocks.block51_5.handler51_5 import cache37 as cache551
from information_blocks.block11 import infohandler11
from information_blocks.block4 import infohandler4_01
from information_blocks.block6_3_1 import infohandler4_0
from information_blocks.block37 import infohandler6
from information_blocks.block26.infohandler6 import cache as cache26
import time
import getpath
import os
token = gettokenbot.get_token()

path = getpath.pathreturn()

bot = TeleBot(token)
admin_ids = ["902026475", "635863841", "1751965432", "73262536", "1184924981", "8128066387"]

@bot.message_handler(commands=['skip2'])
def asdasd(message: Message):
    handler311.block4_31(message, bot)
@bot.message_handler(commands=['skip'])
def asdasd(message: Message):
    handler73_5.block4_40_1(message, bot)
def multi_send(text, message):
    ids = 0
    for i in os.listdir(f"{path}"):
        try:
            ida = i.split("_")[0]
            bot.send_message(ida, f"{text.text}")
            ids += 1
        except Exception as e:
            pass
    bot.send_message(message.chat.id, f"Успешная отправка\n\nОтправленно вот стольким пользователям: {ids}")
@bot.message_handler(commands=['admin', 'adminpanel'])
def admin_panel(message):
    if str(message.chat.id) not in admin_ids:
        return
    markup = InlineKeyboardMarkup(row_width=1)
    multi = InlineKeyboardButton("Мульти-Рассылка", callback_data="multi_send")
    downloadany = InlineKeyboardButton("Скачать все", callback_data="download_all")
    delete_all = InlineKeyboardButton("Удалить все", callback_data="delete_all")
    item1 = InlineKeyboardButton("◀️ Назад", callback_data="back1")
    markup.add(multi, delete_all, downloadany, item1)
    bot.send_message(message.chat.id, "Админ-Панель\nНа связи кот-бот какие действия нужно выполнить?", reply_markup=markup)
    try:
        bot.delete_message(message.chat.id, message.id)
    except Exception:
        pass


@bot.message_handler(commands=["start"])
def start(message: Message):
    createdb.createdb(message.chat.id)
    markup = InlineKeyboardMarkup(row_width=1)
    item1 = InlineKeyboardButton("Начать Заполнение", callback_data="start_filling")
    item2 = InlineKeyboardButton("Зачем это все", callback_data="why")
    item3 = InlineKeyboardButton("Видео про проектирование", callback_data="video")

    markup.add(item1, item2, item3)

    bot.send_photo(
        message.chat.id,
        InputFile("main_photo/comanda.jpg"),
        "<b>🔵 Добрый день!</b>\n\n"
        "На связи команда IVAN DOM Rostov\n\n"
        "Мы здесь, чтобы помочь вам заполнить анкету для техзадания на проектирование вашего будущего дома.\n\n"
        "Это один из важнейших документов будущей стройки. А ещё – классная возможность лучше понять свои мечты, планы и цели.\n\n"
        "Всего несколько шагов – и вы приблизитесь к дому мечты.\n"
        "Вам понадобится коллективное мнение всех членов семьи, немного терпения и пару часов свободного времени.\n"
        "А мы и наша служба заботы всегда на связи, и готовы помочь с любыми вопросами по содержанию анкеты.\n\n"
        "<b>Если готовы – предлагаем начать!</b>",
        parse_mode="HTML",
        reply_markup=markup
    )


def write_to_excel(message):
    filename = f"datausers/{message.chat.id}.txt"
    reading_file = open(f"{path}/{message.chat.id}_id", "r", encoding="utf-8")
    data = reading_file.readline().replace("NULL", "Вопрос Пропущен").replace("%"," ").split(", ")
    with open(filename, "w", encoding="utf-8") as a:
        a.write(f"ID Пользователя: \n{data[0]}\n\n"
                f"Номер Телефона: \n{data[1]}\n\n"
                f"Имя И Фамилия: \n{data[2]}\n\n"
                f"Почта: \n{data[3]}\n\n"
                f"Выберите самые важные цели вашего строительства: \n{data[4]}\n\n"
                f"Давайте уточним, какие еще результаты важны вам в строительстве?: \n{data[5]}\n\n"
                f"Пожалуйста, в ответном сообщении опишите други свои цели, что мы не упомянули: \n{data[6]}\n\n"
                f"Что для вас наиболее ценно и важно в доме?: \n{data[7]}\n\n"
                f"Расскажите о важном: \n{data[8]}\n\n"
                f"Кто будет жить в будущем доме: \n{data[9]}\n\n"
                f"Пожалуйста, в ответном сообщении расскажите, кто ещё будет проживать в вашем новом доме: \n{data[10]}\n\n"
                f"Категория вашего дома: \n{data[11]}\n\n"
                f"Какой площади вы хотите построить дом: \n{data[12]}\n\n"
                f"Какой этажности будет дом: \n{data[13]}\n\n"
                f"Будет ли в доме цокольный этаж: \n{data[14]}\n\n"
                f"Какой архитектурный стиль выберете для своего дома: \n{data[15]}\n\n"
                f"Расскажите о своём видении архитектурного стиля будущего дома: \n{data[16]}\n\n"
                f"Добавим вашему будущему дому особенный характер: \n{data[17]}\n\n"
                f"Пожалуйста, в ответном сообщении расскажите о других деталях будущего дома: \n{data[18]}\n\n"
                f"Какие материалы вы выберете для отделки фасадов своего дома: \n{data[19]}\n\n"
                f"Пожалуйста, в ответном сообщении расскажите нам об особых пожеланиях к отделке фасадов: \n{data[20]}\n\n"
                f"Как вы видите кровлю своего дома: \n{data[21]}\n\n"
                f"Пожелания к кровле: \n{data[22]}\n\n"
                f"Пожалуйста, отметьте, какие помещения в вашем доме точно включены в зону прихожей: \n{data[23]}\n\n"
                f"Пожелания к входной зоне: \n{data[24]}\n\n"
                f"Пожалуйста, в ответном сообщении укажите желаемую площадь зоны прихожей: \n{data[25]}\n\n"
                f"Сердце дома: \n{data[26]}\n\n"
                f"Пожалуйста, в ответном сообщении укажите желаемую площадь зоны гостиной: \n{data[27]}\n\n"
                f"Пожалуйста, в ответном сообщении укажите примерную желаемую площадь зоны кухни: \n{data[28]}\n\n"
                f"Пожалуйста, в ответном сообщении укажите желаемую площадь террасы: \n{data[29]}\n\n"
                f"Пожалуйста, в ответном сообщении расскажите нам о своих пожеланиях к центральной зоне дома: \n{data[30]}\n\n"
                f"Мастер-спальня — ваш личный оазис спокойствия: \n{data[31]}\n\n"
                f"Пожалуйста, в ответном сообщении укажите желаемую площадь мастер-спальни: \n{data[32]}\n\n"
                f"Пожалуйста, в ответном сообщении расскажите нам о своих пожеланиях к зоне мастер-спальни: \n{data[33]}\n\n"
                f"Сколько комнат вы планируете в зоне детских: \n{data[34]}\n\n"
                f"Какие ещё комнаты вы планируете в зоне детских: \n{data[35]}\n\n"
                f"Пожалуйста, в ответном сообщении укажите желаемую среднюю площадь детской спальни: \n{data[36]}\n\n"
                f"Пожалуйста, в ответном сообщении расскажите нам о своих пожеланиях к зоне детских: \n{data[37]}\n\n"
                f"Зона для гостей: какие помещения для неё необходимы: \n{data[38]}\n\n"
                f"Пожалуйста, в ответном сообщении укажите желаемую среднюю площадь гостевой: \n{data[39]}\n\n"
                f"Пожалуйста, в ответном сообщении расскажите нам о своих пожеланиях к гостевой зоне: \n{data[40]}\n\n"
                f"Сколько планируете санузлов в доме, включая туалетные, ванные комнаты и душевые?: \n{data[41]}\n\n"
                f"Пожалуйста в ответном сообщении укажите ориентировочную площадь санузла (санузел в мастер-спальне): \n{data[42]}\n\n"
                f"Пожалуйста, выберите наполнение санузла: \n{data[43]}\n\n"
                f"Пожалуйста, в ответном сообщении укажите ориентировочную площадь санузла: \n{data[44]}\n\n"
                f"Пожалуйста, выберите наполнение санузла: \n{data[45]}\n\n"
                f"Пожалуйста, в ответном сообщении укажите ориентировочную площадь санузла: \n{data[46]}\n\n"
                f"Пожалуйста, выберите наполнение санузла: \n{data[47]}\n\n"
                f"Пожалуйста, в ответном сообщении укажите ориентировочную площадь санузла: \n{data[48]}\n\n"
                f"Пожалуйста, выберите наполнение санузла: \n{data[49]}\n\n"
                f"Пожалуйста, в ответном сообщении расскажите нам о дополнительных пожеланиях к зоне санузлов: \n{data[50]}\n\n"
                f"Пожалуйста, отметьте, что войдёт в состав вашего домашнего пространства для работы и саморазвития: \n{data[51]}\n\n"
                f"Пожалуйста, в ответном сообщении укажите ориентировочную площадь кабинета: \n{data[52]}\n\n"
                f"Пожалуйста, в ответном сообщении расскажите нам о своих пожеланиях к пространству для работы: \n{data[53]}\n\n"
                f"Обсудим хозяйственную зону: \n{data[54]}\n\n"
                f"Пожалуйста в ответном сообщении укажите ориентировочную площадь котельной: \n{data[55]}\n\n"
                f"Пожалуйста в ответном сообщении укажите ориентировочную площадь хозблока внутри дома: \n{data[56]}\n\n"
                f"Пожалуйста в ответном сообщении расскажите о хозяйственно-бытовой зоне: \n{data[57]}\n\n"
                f"Какие пространства в своём доме вы бы хотели запланировать: \n{data[58]}\n\n"
                f"Пожалуйста, в ответном сообщении расскажите нам о своих пожеланиях к тематическим пространствам дома: \n{data[59]}\n\n"
                f"Пожалуйста, укажите комфортный для вас уровень чистового пола первого этажа: \n{data[60]}\n\n"
                f"Укажите желаемую высоту потолков комнат первого этажа: \n{data[61]}\n\n"
                f"Укажите желаемую высоту потолков комнат второго этажа: \n{data[62]}\n\n"
                f"Укажите желаемую высоту потолков помещений в цоколе: \n{data[63]}\n\n"
                f"Выберите объекты базового комфорта, необходимые вам на своём участке: \n{data[64]}\n\n"
                f"Выберите объекты в зоне отдыха и релакса?: \n{data[65]}\n\n"
                f"Пожалуйста, выберите стиль ландшафтного дизайна, который вам ближе всего: \n{data[66]}\n\n"
                f"Пожалуйста, в ответном сообщении расскажите нам о своих пожеланиях и идеях по организации пространства вокруг дома: \n{data[67]}\n\n"
                f"У вас уже приобретён участок?: \n{data[68]}\n\n"
                f"Пожалуйста, в ответном сообщении укажите кадастровый номер участка: \n{data[69]}\n\n"
                f"Пожалуйста, в ответном сообщении укажите площадь участка: \n{data[70]}\n\n"
                f"Пожалуйста, в ответном сообщении укажите адрес / месторасположение участка: \n{data[71]}\n\n"
                f"На участке есть уклон?: \n{data[72]}\n\n"
                f"Как обстоят дела с подъездом к участку: \n{data[73]}\n\n"
                f"Какие коммуникации есть/ проходят по меже участка?: \n{data[74]}\n\n"
                f"Есть ли актуальный градостроительный план участка?: \n{data[75]}\n\n"
                f"Есть ли у участка ограничения на строительство по градостроительному плану: \n{data[76]}\n\n"
                f"Есть ли на участке линии центральных коммуникаций, ограничивающие пользование: \n{data[77]}\n\n"
                f"Выполнена ли топосъемка для данного участка: \n{data[78]}\n\n"
                f"Какие подготовительные работы необходимо провести на участке: \n{data[79]}\n\n"
                f"Пожалуйста, в ответном сообщении напишите о других известных вам особенностях участка, которые важно учитывать (ситуация на соседних участках, соседи, прочие особенности): \n{data[80]}\n\n"
                f"Пожалуйста, в ответном сообщении напишите ориентировочную дату, когда хотите начать строительство: \n{data[81]}\n\n"
                f"Пожалуйста, в ответном сообщении напишите желаемую дату новоселья: \n{data[82]}\n\n"
                f"Самое важное в проектировании дома: \n{data[83]}\n\n"
                f"Что для вас самое важное в процессе строительства дома: \n{data[84]}\n\n"
                f"Для чего вы строите дом: \n{data[85]}\n\n"
                f"Что в процессе строительства вы оцените выше всего: \n{data[86]}\n\n"
                f"Окончательные пожелания: \n{data[87]}\n\n")
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(InlineKeyboardButton("Скачать все", callback_data="download_all"))
        bot.send_message(902026475, f"{message.chat.id}, {message.chat.username} прошел анкету", reply_markup=markup)
        bot.send_message(8128066387, f"{message.chat.id}, {message.chat.username} прошел анкету", reply_markup=markup)
        
@bot.callback_query_handler(func=lambda call: True)
def callback_start(call: CallbackQuery):
    # хандлим отправку
    if call.data == "send_anket":
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(InlineKeyboardButton("Подписаться на ТГ-канал", url="https://t.me/ivandomrosrov"))
        bot.send_message(call.message.chat.id, 
                         "<b>🔵 Пользы много не бывает!</b>\n\n"
                         "Чтобы у вас было больше экспертной информации о строительстве, подготовили для вас дайджест наших публикаций:\n\n"
                         "#idrстроительство@ivandomrosrov – всё про цены, ситуацию на рынке\n"
                         "#idrпроектирование@ivandomrosrov – посты о проектировании и нашем подходе к созданию вашего комфорта\n"
                         "#категориидомов@ivandomrosrov – подборка информации об особенностях домов классов комфорт, бизнес и премиум\n"
                         "#дизайниотделка@ivandomrosrov – всё про самый долгожданный этап каждой стройки\n"
                         "#какмыстроим@ivandomrosrov – реалити-шоу о том, как рождаются дома наших заказчиков\n"
                         "#пробизнес@ivandomrosrov – босс IVAN DOM Rostov, Иван Чернявский, делится мыслями о предпринимательстве\n"
                         "#стильжизнипредприниматель@ivandomrosrov – немного лайф-контента\n"
                         "#строймемы@ivandomrosrov – котики, шуточки и наш менеджер по красоте рассказывают о стройке без стресса и страданий",
                         parse_mode="HTML", reply_markup=markup)
        write_to_excel(call.message)
    # хандлим админку
    filepath = "datausers/"
    if call.data == "download_all":
        zip_path = os.path.join(filepath, "zip.zip")
        with zipfile.ZipFile(zip_path, "w") as zipf:
            for filename in os.listdir(filepath):
                file_path = os.path.join(filepath, filename)
                if os.path.isfile(file_path) and filename != "zip.zip":
                    zipf.write(file_path, arcname=filename)
        with open(zip_path, "rb") as f:
            bot.send_document(call.message.chat.id, f, caption="Все анкеты в одном архиве")
        os.remove(zip_path)
    if call.data == "delete_all":
        for i in os.listdir(filepath):
            file_path = os.path.join(filepath, i)
            if os.path.isfile(file_path):
                os.remove(file_path)
        else:
            bot.send_message(call.message.chat.id, "Успешно")


    return_path = {
    "3": lambda: handler3.block4_3(call.message, bot),
    "4": lambda: handler4.block4_4(call.message, bot),
    "464": lambda: handler451.block4_6(call.message, bot),
    "6": lambda: handler6.block4_6(call.message, bot),
    "8": lambda: handler8.block4_8(call.message, bot),
    "9": lambda: handler9.block4_9(call.message, bot),
    "11": lambda: handler11.block4_11(call.message, bot),
    "12": lambda: handler12.block4_12(call.message, bot),
    "121": lambda: handler12_1.block4_12_1(call.message, bot),
    "13": lambda: handler13.block4_13(call.message, bot),
    "14": lambda: handler14.block4_11(call.message, bot),
    "15": lambda: handler15.block4_9(call.message, bot),
    "16": lambda: handler16.block4_11(call.message, bot),
    "17": lambda: handler17.block4_9(call.message, bot),
    "18": lambda: handler18.block4_11(call.message, bot),
    "19": lambda: handler19.block4_9(call.message, bot),
    "20": lambda: handler20.block4_11(call.message, bot),
    "22": lambda: handler22.block4_11(call.message, bot),
    "205": lambda: handler20_5.block4_21(call.message, bot),
    "221": lambda: handler233.block4_11(call.message, bot),
    "225": lambda: handler233.block4_11(call.message, bot),
    "26": lambda: handler26.block4_26(call.message, bot),
    "29": lambda: handler29.block4_28(call.message, bot),
    "30": lambda: handler30.block4_30(call.message, bot),
    "33": lambda: handler33.block4_32(call.message, bot),
    "36": lambda: handler36.block4_36(call.message, bot),
    "38": lambda: handler38.block4_38(call.message, bot),
    "40": lambda: handler40.block4_40(call.message, bot),
    "42": lambda: handler42.block4_40(call.message, bot),
    "45": lambda: handler45.block4_40(call.message, bot),
    "455": lambda: handler45_5.block4_46(call.message, bot),
    "47": lambda: handler47.block4_40(call.message, bot),
    "475": lambda: handler47_5.block4_40(call.message, bot),
    "51": lambda: handler51.block4_40(call.message, bot),
    "515": lambda: handler51_5.block4_52(call.message, bot),
    "534": lambda: handler53_4.block4_53(call.message, bot),
    "535": lambda: handler53_5.block4_54(call.message, bot),
    "54": lambda: handler54.block4_54(call.message, bot),
    "545": lambda: handler54_5.block4_55(call.message, bot),
    "55": lambda: handler55.block4_55(call.message,bot),
    "555": lambda: handler55_5.block4_56(call.message, bot),
    "57": lambda: handler57.block4_57(call.message, bot),
    "62": lambda: handler62.block4_40(call.message, bot),
    "63": lambda: handler63.block4_40(call.message, bot),
    "64": lambda: handler64.block4_46(call.message, bot),
    "65": lambda: handler65.block4_40(call.message, bot),
    "66": lambda: handler66.block4_40(call.message, bot),
    "67": lambda: handler67.block4_40(call.message, bot),
    "72": lambda: handler72.block4_40(call.message, bot),
    "73": lambda: handler73.block4_40(call.message, bot),
    "731": lambda: handler73.block4_40(call.message, bot),
    "735": lambda: handler73_5.block4_40_1(call.message, bot),
    "74": lambda: handler74.block4_40(call.message, bot),
    "75": lambda: handler75.block4_40(call.message, bot),
    "76": lambda: handler76.block4_40(call.message, bot)
    }
    if call.data.startswith("return"):
        func = return_path.get(call.data.split("_")[1], None)
        if func:
            func()



    if call.data == "why":
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = InlineKeyboardMarkup()
        item2 = InlineKeyboardButton("Велком Видео", url="https://rutube.ru/video/private/704a3498b57291285dc22443ca8f9f2a/?p=LdXnNQ4synFFnSKpe5bD_w")
        item1 = InlineKeyboardButton("◀️ Назад", callback_data="back1")
        markup.add(item2, item1)
        bot.send_message(
            call.message.chat.id,
            "<b>🔵 Что вы получите, заполнив анкету для техзадания?</b>\n\n"
            "Точное соответствие вашим ожиданиям: ваши подробные ответы помогают нашим архитекторам и проектировщикам создать проект, идеально отвечающий вашим пожеланиям.\n\n"
            "Экономию времени: заранее заполненная анкета на 60% сократит количество встреч и уточнений, необходимых для разработки проекта.\n\n"
            "Персонализированный подход: мы сможем учесть все важные именно для вас детали: от вашего ритма жизни и любимых зон отдыха до удобного расположения выключателей и систем умного дома.\n\n"
            "Прозрачность процесса: анкета структурирует взаимодействие между вами и нашей командой. Вы получаете более понятные и предсказуемые.\n\n"
            "<i>Инвестируйте 60 минут в безупречный комфорт дома, который знает о вас больше, чем вы сами!</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "video":
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = InlineKeyboardMarkup()
        item2 = InlineKeyboardButton("◀️ Назад", callback_data="back1")
        item1 = InlineKeyboardButton("Видео про проектирование", url="https://rutube.ru/video/private/5d04a6b7f94569f4117b9834f00b3524/?p=MxKf9MunczD6Buv5-fImmw")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(
            call.message.chat.id,
            "<b>🔵 Видео про проектирование частных домов с IVAN DOM Rostov</b>\n\n"
            "<i>Посмотрите короткое видео о том, как мы подходим к проектированию и что важно учесть на старте!</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "start_filling":
        bot.delete_message(call.message.chat.id, call.message.id)
        infohandler4_01.infoblock6_3(call.message, bot)
    if call.data == "back1":
        bot.delete_message(call.message.chat.id, call.message.id)
        start(call.message)
    if call.data == "skip_4_9":
        handler9.block4_9(call.message, bot)
    if call.data == "skip_19_1":
        handler20.block4_11(call.message, bot)
    if call.data == "skip3_4":
        handler37.block4_37(call.message, bot)
    if call.data == "multi_send":
        markup = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        markup.add(KeyboardButton("Назад"))
        a = bot.send_message(call.message.chat.id, "Введите текст для рассылки", reply_markup=markup)
        bot.register_next_step_handler(a, lambda msg: multi_send(msg, call.message))
    markup = InlineKeyboardMarkup()
    backs = InlineKeyboardButton("◀️ Назад", callback_data="back11")
    if call.data == "goto4_10":
        handler10.block4_10(call.message, bot)
    if call.data == "back11":
        bot.delete_message(call.message.chat.id, call.message.id)
        handler9.block4_9(call.message, bot)
    if call.data == "biznes":
        markup.add(backs)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/busin.jpg"),
            "🔵 <b>ДОМА БИЗНЕС-КЛАССА</b>\n\n"
            "Кредо дома класса БИЗНЕС – повышенный комфорт и функциональность.\n\n"
            "Это пространство для роста. Такой дом развивает амбиции, цели, личность.\n\n"
            "Все детали здесь продуманы для удобства жизни.\n\n"
            "Это удачная инвестиция: благодаря повышенной надёжности и долговечности дом со временем только растёт в цене.\n\n"
            "<b>Диапазон стоимости:</b> 68 900 – 94 700₽/м2 ",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "comfort":
        markup.add(backs)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id,InputFile("main_photo/comf.jpg"), "🔵<b>ДОМА КОМФОРТ-КЛАССА</b>\n\n"
            "Оптимальное сочетание цены и качества. Простые и надежные решения без лишних затрат.\n\n"
            "Такой дом – достойный выбор в балансе «цена – качество».\n\n"
            "<b>Диапазон стоимости:</b> 54 700 –68 200 ₽/ м2 ",
            parse_mode="HTML",
            reply_markup=markup)
    if call.data == "premium":
        markup.add(backs)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/prem.jpg"),
            "🔵 <b>ДОМА ПРЕМИУМ-КЛАССА</b>\n\n"
            "У таких домов, как у людей, есть имена. И собственная неповторимая черта, «фишка»: единение с ландшафтом, терраса, летящая над бухтой, атмосфера итальянских палаццо – то, что зажигает именно вас. Это дома-статус. Дома-актив. Особенный мир, воплощённый в жизнь из вашей смелой идеи командой профессионалов. Для их создания мы используем только премиальные материалы, а проектирование заточено на ваш безупречный комфорт.\n\n"
            "Жизнь в таком доме дарит максимальный уровень удобства и эстетики.\n\n"
            "<b>Диапазон стоимости:</b> от 98 300₽/ м2",
            parse_mode="HTML",
            reply_markup=markup
        )
    
    if call.data == "podrobnee1":
        handler13.block4_13(call.message, bot)
    if call.data == "podrobnee2":
        handler15.block4_9(call.message, bot)
    if call.data == "podrobnee3":
        handler17.block4_9(call.message, bot)
    if call.data == "podrobnee4":
        handler19.block4_9(call.message, bot)
    if call.data == "podrobnee5":
        handler20_5.block4_21(call.message, bot)
    if call.data == "podrobnee6":
        handler311.block4_31(call.message, bot)
    if call.data == "podrobnee7":
        handler51_5.block4_52(call.message, bot)
    if call.data == "podrobnee8":
        handler53_5.block4_54(call.message, bot)
    if call.data == "podrobnee9":
        handler55_5.block4_56(call.message, bot)
    if call.data == "podrobnee10":
        handler54_5.block4_55(call.message, bot)
    if call.data == "podrobnee11":
        handler45_5.block4_46(call.message, bot)
    if call.data == "podrobnee22":
        handler9.block4_9(call.message, bot)
        




    if call.data == "asdfsafasdfasdf":
        infohandler6.infoblock9_0(call.message, bot)
        bot.delete_message(call.message, bot)

    #ответы тут карочше дада
    if call.data == "biznes1":
        createdb.exdb("Бизнес-Класс", 11, call.message.chat.id)
        infohandler4_0.infoblock6_3(call.message, bot)
    if call.data == "comfort1":
        createdb.exdb("Комфорт-Класс", 11, call.message.chat.id)
        infohandler4_0.infoblock6_3(call.message, bot)
    if call.data == "premium1":
        createdb.exdb("Премиум-Класс", 11, call.message.chat.id)
        infohandler4_0.infoblock6_3(call.message, bot)


    if call.data == "onefloor":
        # writedata11(call.message, call.data)
        createdb.exdb("Рассматриваю одноэтажные проекты", 13, call.message.chat.id)
        handler12_1.block4_12_1(call.message, bot)
    if call.data == "twofullfloor":
        createdb.exdb("Двухэтажный с полным вторым этажом", 13, call.message.chat.id)
        handler12_1.block4_12_1(call.message, bot)
        # writedata11(call.message, call.data)
    if call.data == "mansard":
        createdb.exdb("Нравятся дома с мансардами", 13, call.message.chat.id)
        handler12_1.block4_12_1(call.message, bot)
        # writedata11(call.message, call.data)
    if call.data == "after_architect":
        createdb.exdb("NULL", 13, call.message.chat.id)
        handler12_1.block4_12_1(call.message, bot)
        # writedata11(call.message, call.data)

    if call.data == "backs123":
        handler13.block4_13(call.message, bot)
    backs = InlineKeyboardButton("◀️ Назад", callback_data="backs123")
    if call.data == "neoclassic":
        markup = InlineKeyboardMarkup()
        markup.add(backs)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/neoclass.jpg"),
            "🔵 <b>Неоклассика</b>\n\n"
            "Представьте дом, где гармония и элегантность сливаются воедино: строгие симметричные фасады, колонны, лепнина и благородные натуральные материалы.\n\n"
            "<b>Неоклассика</b> — это вечная красота, вдохновлённая дворцами прошлого, но адаптированная для современной жизни.\n\n"
            "<i>Ваш дом станет воплощением аристократического стиля, где каждая деталь говорит о безупречном вкусе.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "wright":
        markup = InlineKeyboardMarkup()
        markup.add(backs)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, InputFile("main_photo/rayta.jpg"),"🔵 <b>Стиль Райта</b>\n\n"
            "Дом в стиле Райта — это гармония с природой: низкие горизонтальные линии, плоские крыши, панорамные окна и натуральные материалы. Архитектура не противостоит ландшафту, а становится его продолжением. Такой дом создаёт ощущение уюта, свободы и единения с окружающим миром.\n\n"
            "<i>Идеальный выбор для тех, кто ценит естественность и продуманный минимализм.</i>",
            parse_mode="HTML",
            reply_markup=markup)
    if call.data == "hi_tech":
        markup = InlineKeyboardMarkup()
        markup.add(backs)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/hteh.jpg"),
            "🔵 <b>Hi-Tech</b>\n\n"
            "Смелые линии, стекло, металл и инновационные технологии — дом в стиле Hi-Tech выглядит как произведение будущего.\n\n"
            "Большие панорамные окна, открытые пространства и умные инженерные решения делают его не просто жильём, а высокотехнологичным пространством для жизни.\n\n"
            "<i>Если вы любите современность, функциональность и дерзкий дизайн — этот стиль для вас.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "chale":
        markup = InlineKeyboardMarkup()
        markup.add(backs)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/shale.jpg"),
            "🔵 <b>Шале</b>\n\n"
            "Тёплый, уютный дом с массивными деревянными балками, каменными стенами и покатой крышей — стиль шале словно создан для отдыха и умиротворения.\n\n"
            "Он напоминает о горных курортах, где можно укрыться от суеты и наслаждаться природой.\n\n"
            "<i>Такой дом дарит ощущение надёжности, тепла и спокойствия в любое время года.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "barnhouse":
        markup = InlineKeyboardMarkup()
        markup.add(backs)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/bhous.jpg"),
            "🔵 <b>Барнхаус</b>\n\n"
            "Простота, функциональность и эстетика минимализма — барнхаус сочетает в себе лаконичные формы и уют.\n\n"
            "Дом напоминает переосмысленный деревенский вайб: открытые пространства, натуральные материалы, большие окна и чёткие линии.\n\n"
            "<i>Это стиль для тех, кто ценит свободу, свет и естественность без лишних деталей.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "scandinavian":
        markup = InlineKeyboardMarkup()
        markup.add(backs)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/scandy.jpg"),
            "🔵 <b>Скандинавский стиль</b>\n\n"
            "Светлый, просторный и невероятно уютный дом, где главное — естественность и комфорт.\n\n"
            "Дерево, пастельные тона, панорамные окна и функциональная мебель создают атмосферу тепла и гармонии.\n\n"
            "<i>Скандинавский стиль — это про лаконичную красоту, близость к природе и ощущение дома, где хочется жить.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "unique":
        markup = InlineKeyboardMarkup()
        markup.add(backs)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/uniq.jpg"),
            "🔵 <b>Уникальный стиль</b>\n\n"
            "Ваш дом — это отражение вашей личности, и он не обязан вписываться в рамки.\n\n"
            "Смешение стилей, нестандартные формы, эксперименты с материалами и планировками — всё возможно!\n\n"
            "Мы поможем воплотить самые смелые идеи, чтобы ваш дом стал по-настоящему особенным.\n\n"
            "<i>Давайте создадим нечто уникальное вместе!</i>",
            parse_mode="HTML",
            reply_markup=markup
        )

    # хандлим данные




    if call.data == "neoclassic1":
        createdb.exdb("Неоклассика", 15, call.message.chat.id)
        handler14.block4_11(call.message, bot)

    if call.data == "wright1":
        createdb.exdb("Стиль Райта", 15, call.message.chat.id)
        handler14.block4_11(call.message, bot)
    if call.data == "hi_tech1":
        createdb.exdb("Hi-Tech", 15, call.message.chat.id)
        handler14.block4_11(call.message, bot)
    if call.data == "chale1":
        createdb.exdb("Шале", 15, call.message.chat.id)
        handler14.block4_11(call.message, bot)
    if call.data == "barnhouse1":
        createdb.exdb("Барнхаус", 15, call.message.chat.id)
        handler14.block4_11(call.message, bot)
    if call.data == "scandinavian1":
        createdb.exdb("Скандинавский", 15, call.message.chat.id)
        handler14.block4_11(call.message, bot)
    if call.data == "unique1":
        createdb.exdb("Уникальный стиль", 15, call.message.chat.id)
        handler14.block4_11(call.message, bot)

    back = InlineKeyboardButton("◀️ Назад", callback_data="backwaw")
    if call.data == "backwaw":
        handler15.block4_9(call.message, bot)
    if call.data == "panoramic":
        markup = InlineKeyboardMarkup()
        markup.add(back)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/panok.jpg"),
            "🔵 <b>Панорамные окна</b>\n\n"
            "Представьте, как в ваш дом врывается свет и пейзажи: панорамные окна стирают границу между интерьером и природой. Они делают пространство визуально больше, наполняют его воздухом и создают ощущение свободы. Утро с чашечкой кофе у такого окна — уже маленькое путешествие.\n\n"
            "<i>Хотите жить в гармонии с окружающим миром? Это идеальное решение!</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "second_light":
        markup = InlineKeyboardMarkup()
        markup.add(back)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/seclig.jpg"),
            "🔵 <b>Второй свет</b>\n\n"
            "Двухэтажное пространство без перекрытий — второй свет – дарит дому роскошь простора и торжественность. Высокие потолки, игра света и воздуха, эффектные люстры или естественное освещение через окна создают неповторимую атмосферу.\n\n<i>Это выбор тех, кто ценит размах, элегантность и чувство простора даже в камерной гостиной.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "patio":
        markup = InlineKeyboardMarkup()
        markup.add(back)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/plcr.jpg"),
            "🔵 <b>Плоская кровля с зоной отдыха</b>\n\n"
            "Ваша крыша — это не просто защита от дождя, а дополнительное пространство для жизни!\n\n"
            "Плоская кровля с зоной отдыха превращается в террасу с видом на звёзды, место для летних вечеринок или уединённого чаепития.\n\n"
            "<i>Добавьте озеленение, шезлонги или даже мини-бассейн — и вы получите идеальное место для релакса.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "bay_window":
        markup = InlineKeyboardMarkup()
        markup.add(back)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/erker.jpg"),
            "🔵 <b>Эркер</b>\n\n"
            "Эркер — это архитектурное «объятие»: выступающая часть дома с окнами создаёт уютный уголок, наполненный светом.\n\n"
            "Здесь можно устроить зимний сад, каминную зону или место для чтения с панорамным видом.\n\n"
            "<i>Эркер добавляет дому индивидуальности и делает планировку интереснее.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "atrium":
        markup = InlineKeyboardMarkup()
        markup.add(back)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/atrium.jpg"),
            "🔵 <b>Атриум</b>\n\n"
            "Сердце дома, пронизанное светом: атриум — это открытое пространство от первого этажа до крыши, вокруг которого строится жизнь.\n\n"
            "Внутренний дворик, зимний сад или просто воздушная «витрина» вашего интерьера — он создаёт ощущение простора и связывает этажи в единую композицию.\n\n"
            "<i>Атриум — это не просто пространство, а элемент архитектуры, который делает дом уютным и функциональным.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "balcony":
        markup = InlineKeyboardMarkup()
        markup.add(back)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/balkon.jpg"),
            "🔵 <b>Балкон</b>\n\n"
            "Ваш личный уголок на свежем воздухе: балкон может быть мини-садом, местом для завтрака или точкой с лучшим видом на окрестности.\n\n"
            "<i>Открытый или застеклённый, компактный или просторный — он добавляет дому шарма и функциональности.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "basement":
        markup = InlineKeyboardMarkup()
        markup.add(back)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/podval.jpg"),
            "🔵 <b>Подвал</b>\n\n"
            "Небольшое помещение площадью до 20 м², где обычно хранят продукты на зиму или используют как место для хранения.\n\n"
            "<i>Чаще всего организация подвала характерна для домов комфорт-класса. При прочих равных организовать подвал под отдельно стоящим хозблоком дешевле, чем в доме.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )

    if call.data == "backwaw212":
        handler17.block4_9(call.message, bot)
    
    ceramic_brick = InlineKeyboardButton("◀️ Назад", callback_data="backwaw212")
    if call.data == "ceramic_brick":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/ceramcopy.jpg"),
            "🔵 <b>Кирпич керамический</b>\n\n"
            "Тёплый, прочный и дышащий — керамический кирпич создаёт фасад, который выглядит благородно десятилетиями.\n"
            "Его натуральные оттенки, от медового до терракотового, придают дому уютную солидность.\n\n"
            "<i>Идеальный выбор для тех, кто ценит классическую красоту, экологичность и долговечность без лишнего пафоса.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "handmade_brick":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id,InputFile("main_photo/handmade.jpg"), "🔵 <b>Кирпич ручной формовки</b>\n\n"
            "Фасад с историей: каждый кирпич ручной формовки уникален благодаря неровным краям и состаренной текстуре. Такой материал придаёт дому аутентичный шарм старинной усадьбы или европейского особняка.\n\n"
            "<i>Если вы мечтаете о доме с характером и душевной теплотой — это ваш вариант.</i>",
            parse_mode="HTML",
            reply_markup=markup)
    if call.data == "handmade_riegel":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id,
                       InputFile("main_photo/rigelruchaskdf.jpg"),
                        "🔵 <b>Ригель ручной формовки</b>\n\n"
            "Элитная кирпичная кладка с выразительной рельефной поверхностью: ригель ручной формовки добавляет фасаду глубины и аристократизма. Его используют для акцентных элементов — арок, колонн или цоколей, создавая эффект «наслоения времён».\n\n"
            "<i>Дом с таким фасадом выглядит дорого и стильно.</i>",
            parse_mode="HTML",
            reply_markup=markup)
    if call.data == "decorative_plaster":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id,
                       InputFile("main_photo/dekaraasldfaskjfdlaskdjf.jpg"), "🔵 <b>Декоративная штукатурка</b>\n\n"
            "Бесконечное поле для творчества: штукатурка может быть гладкой, фактурной, цветной или с эффектом натурального камня. Она позволяет реализовать любые стили — от средиземноморского до хай-тека, легко ремонтируется и «дышит».\n\n"
            "<i>Идеальна для тех, кто хочет индивидуальный фасад без сложного ухода.</i>",
            parse_mode="HTML",
            reply_markup=markup)
    if call.data == "natural_wood":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/wood.jpg"),
            "🔵 <b>Натуральное дерево</b>\n\n"
            "Тепло, экологичность и живая текстура: деревянный фасад создаёт ощущение единения с природой. Современные пропитки защищают материал от влаги и повреждений микроорганизмами, сохраняя его красоту на годы. Вариантов масса — от бруса до планкена, от скандинавской лаконичности до стиля шале.\n\n"
            "<i>Дом, который пахнет лесом и уютом!</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "natural_stone":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, InputFile("main_photo/prca.jpg"),"🔵 <b>Природный камень</b>\n\n"
            "Солидность, которая не выходит из моды: гранит, сланец, песчаник или известняк придают фасаду монументальность и роскошь. Камень сочетается с любыми стилями — от классики до модерна, а его долговечность исчисляется веками.\n\n"
            "<i>Ваш дом будет выглядеть как родовой оплот!</i>",
            parse_mode="HTML",
            reply_markup=markup)
    if call.data == "facade_panels":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/faspal.jpg"),
            "🔵 <b>Фасадные панели</b>\n\n"
            "Панели сайдингового типа – типичный выбор для домов эконом-класса: панели имитируют кирпич, камень или дерево, но легче и дешевле натуральных материалов. Они устойчивы к погоде, быстро монтируются, но проигрывают в эстетике.\n\n"
            "<i>Панели более дорогих категорий (фиброцемент и т.п.) часто используются для комбинированной отделки фасадов домов бизнес-класса.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "flexible_ceramics":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/gbcer.jpg"),
            "🔵 <b>Гибкая керамика</b>\n\n"
            "Инновация в мире фасадов: тонкие керамические плитки на гибкой основе повторяют фактуру натурального камня, дерева или кирпича, но весят в разы меньше. Они не трескаются и крепятся даже на сложные криволинейные поверхности.\n\n"
            "<i>Дом будущего с лёгкостью настоящего!</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    ceramic_brick = InlineKeyboardButton("◀️ Назад", callback_data="rakuzan")

    if call.data == "rakuzan":
        handler19.block4_9(call.message, bot)
    if call.data == "flat_roof":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/plne.jpg"),
            "🔵 <b>Плоская неэксплуатируемая кровля</b>\n\n"
            "Простота и функциональность! Такая кровля подходит для хозяйственных построек, гаражей и современных домов в стиле хай-тек.\n\n"
            "<i>При профессиональном подходе к проектированию и возведению она экономична, быстро монтируется и требует минимального ухода, сохраняя защитные свойства годами.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "notflat_roof":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/asdploskaya.jpg"),
            "<b>🔵 Плоская эксплуатируемая кровля</b>\n\n"
            "Дополнительное пространство для жизни и +100 к стилю.\n\n"
            "На такой кровле можно обустроить зону отдыха, сад или даже парковку.\n\n"
            "<i>Она требует усиленной гидроизоляции и прочного основания, но взамен даёт полезные квадратные метры и уникальный дизайн.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "metal_tile":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/metch.jpg"),
            "🔵 <b>Металлочерепица</b>\n\n"
            "Современная, лёгкая и прочная кровля, которая идеально подходит для любых климатических условий.\n\n"
            "Металлочерепица имитирует классическую черепицу, но при этом долговечна, устойчива к коррозии и проста в монтаже.\n\n"
            "<i>Широкий выбор цветов и профилей позволяет создать стильный и гармоничный облик вашего дома.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "cement_sand_tile":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/cemp.jpg"),
            "🔵 <b>Цементно-песчаная черепица</b>\n\n"
            "Надёжность и элегантность в одном решении.\n\n"
            "Цементно-песчаная черепица обладает высокой прочностью, морозостойкостью и долгим сроком службы.\n\n"
            "<i>Она придаёт дому благородный вид, а её натуральная фактура гармонично вписывается в любой ландшафт.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "ceramic_tile":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/keramich.jpg"),
            "🔵 <b>Керамическая черепица – классика, проверенная веками</b>\n\n"
            "Керамическая черепица — это премиальный выбор для тех, кто ценит натуральные материалы, долговечность и аутентичный европейский стиль.\n\n"
            "<i>Она отлично защищает от шума и сохраняет тепло.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "bitumen_tile":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/gibkaya.jpg"),
            "🔵 <b>Гибкая битумная черепица</b>\n\n"
            "Идеальна для сложных крыш и нестандартных форм.\n\n"
            "Гибкая черепица сочетает лёгкость, прочность и бесшумность. Она устойчива к влаге, ветру и ультрафиолету, а разнообразие цветов и текстур позволяет воплотить любые дизайнерские идеи.",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "composite_tile":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/compp.jpg"),
            "🔵 <b>Композитная черепица</b>\n\n"
            "Современный гибрид металла и битума!\n\n"
            "Композитная черепица объединяет преимущества разных материалов: прочность, лёгкость, тишину во время дождя и реалистичную имитацию натуральной черепицы.\n\n"
            "<i>Отличный выбор для тех, кто хочет долговечность без лишнего веса.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "seam_roof":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/falc.jpg"),
            "🔵 <b>Фальцевая кровля</b>\n\n"
            "Минимализм и надёжность!\n\n"
            "Фальцевая кровля — это гладкие металлические листы с особым замковым соединением, обеспечивающим герметичность.\n\n"
            "<i>Она идеальна для современных проектов, устойчива к нагрузкам и выглядит стильно даже спустя десятилетия.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "with_architect":
        markup = InlineKeyboardMarkup()
        markup.add(ceramic_brick)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, "Вы выбрали: Определим с архитектором", reply_markup=markup)

    # вазврат в 21 хадлер
    if call.data == "nazad":
        handler20_5.block4_21(call.message, bot)

    # хандлим 21 хандлер
    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="nazad")
    markup.add(back)
    if call.data == "prihojaya":
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/prohojaay.jpg"),
            "🔵 <b>Прихожая — первое впечатление о доме</b>\n\n"
            "Здесь важно продумать удобное хранение обуви, верхней одежды и мелочей. Встроенные шкафы, банкетки и зеркала сделают пространство функциональным и стильным.\n\n"
            "<i>Давайте создадим прихожую, которая сделает приятным каждое ваше возвращение домой!</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "garderobnaya":
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/gard.jpg"),
            "🔵 <b>Гардеробная — залог порядка в доме</b>\n\n"
            "Здесь можно систематизировать и упорядочить хранение разместить одежды, аксессуаров, чемоданов и сезонных вещей.\n\n"
            "Встроенные системы хранения, подсветка и зеркала превратят её в идеальное место для сборов.\n\n"
            "<i>Давайте спроектируем гардеробную вашей мечты!</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "sanuzel":
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/sanuasdasdasdel.jpg"),
            "🔵 <b>Санузел в зоне прихожей — +100 баллов к комфорту</b>\n\n"
            "Это заботливо организованное пространство, обеспечивающее комфорт и гигиену с первых шагов в дом.\n\n"
            "<i>Такое решение – про удобство и внимание к комфорту через эргономику.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "lapomoyka":
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/lapomotka.jpg"),
            "🔵 <b>Лапомойка для пушистого любимца</b>\n\n"
            "С ней легко и быстро можно привести питомцев в порядок перед входом в дом.\n\n"
            "<i>Идеальное решение для сохранения чистоты и порядка!</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)

    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="nazad1")
    markup.add(back)


    # хандлим 22.5
    if call.data == "obyedeniti":
        createdb.exdb(call.data, 25, call.message.chat.id)
        handler24.block4_24(call.message, bot)
    if call.data == "razdeliti":
        createdb.exdb(call.data, 25, call.message.chat.id)
        handler24.block4_24(call.message, bot)
    if call.data == "chastichnoobyedeniti":
        createdb.exdb(call.data, 25, call.message.chat.id)
        handler24.block4_24(call.message, bot)
    if call.data == "coydeniticterrasoy":
        createdb.exdb(call.data, 25, call.message.chat.id)
        handler24.block4_24(call.message, bot)
    
    # хандлим 45.5

    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="nazad2")
    markup.add(back)

    if call.data == "nazad2":
        handler45_5.block4_46(call.message, bot)


    if call.data == "cabinet":
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/cab1.jpg"),
            "🔵 <b>Личная зона продуктивности и вдохновения</b>\n\n"
            "Важно продумать удобный рабочий стол, эргономичное кресло и продуманное освещение. "
            "Встроенные полки, звукоизоляция и стильный дизайн помогут создать атмосферу, "
            "в которой легко сосредоточиться.\n\n"
            "<i>Давайте спроектируем кабинет, где каждая идея находит своё воплощение!</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "masterskaya":
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/mast.jpg"),
            "🔵 <b>Место, где творчество обретает жизнь</b>\n\n"
            "Здесь важны прочные поверхности, удобное хранение инструментов и хорошая вентиляция. "
            "Продуманные розетки, освещение и рабочие зоны сделают пространство функциональным и безопасным.\n\n"
            "<i>Вместе мы создадим мастерскую, где ваши идеи будут оживать!</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "biblioteka":
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/bibl.jpg"),
            "🔵 <b>Уголок уединения и погружения в мир книг</b>\n\n"
            "Встроенные стеллажи, уютное кресло и тёплое освещение создадут атмосферу для отдыха, самообразования и развития. Эмоций добавит камин или панорамное окно.\n\n"
            "<i>Спроектируем для вашей семьи особенное пространство для чтения, где каждая книга найдёт своё место, а вы — вдохновение!</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)

    # хандлим 53.5

    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="nazad3")
    markup.add(back)

    if call.data == "nazad3":
        handler53_5.block4_54(call.message, bot)
    
    if call.data == "terrasaudoma":
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/terass.jpg"),
            "🔵 <b>Терраса — это открытая или частично крытая площадка, примыкающая к дому.</b> \n\n"
            "Она может быть с навесом, ограждением, ступенями или без них. Это отличное место для утреннего кофе, семейного ужина или дружеского барбекю. \n\n"
            "<i>Рассмотрите варианты покрытия, освещения и озеленения, чтобы создать своё идеальное пространство для отдыха на свежем воздухе.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "krilcho":
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/krk.jpg"),
            "🔵 <b>Крытое крыльцо защищает вход от осадков и делает его более удобным.</b>\n\n"
            "Оно может быть с козырьком, перилами, ступенями или пандусом.\n\n"
            "<i>Форма, материал отделки и освещение крыльца должно делать вход в дом удобным в любую погоду и, конечно, сочетаться с общим обликом всего домовладения.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "navesavtoprim":
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/nop.jpg"),
            "🔵 <b>Удобный навес защитит автомобиль от непогоды и станет частью экстерьера дома.</b> \n\n"
            "Такое решение экономит место и удобно для быстрой парковки прямо у дома. \n\n"
            "<i>Важно спроектировать его под нужное количество машин, их высоту и конфигурацию (для внедорожников — от 2,5 м). Можно добавить освещение и водоотвод, а еще – вписать навес в общую концепцию.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "navesavto":
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/nod.jpg"),
            "🔵 <b>Свободно стоящий навес для авто</b> – удобное решение, когда въезд на участок расположен на удалении от дома.\n\n"
            "<i>Важно учесть размеры навеса (на 1 или 2 машины), продумать форму (прямой, арочный), материал каркаса и крыши. И конечно, обязательно нужно продумать расположение, чтобы навес не мешал проезду и не портил вид из окон.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "garahprim":
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/garp.jpg"),
            "🔵 <b>Прикрепленный к дому гараж</b> - экономит пространство участка и обеспечивает быстрый доступ к автомобилю.\n\n"
            "Важно продумать размеры, количество машиномест, тип въезда – параллельный или последовательный, и дополнительный функционал (например, хранение инструментов).\n\n"
            "<i>Важнейшие опции в гараже, примыкающем к дому – хорошая вентиляция и отопление.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "garahotdel":
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/garo.jpg"),
            "🔵 <b>Отделённый от основного здания гараж</b> - удобен, когда хочется разделить жилые и хозяйственно-технические зоны.\n\n"
            "<i>При его создании важно обдумать оптимальные габариты, количество мест и необходимые удобства внутри гаража.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "dopgaraj":
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/gdop.jpg"),
            "🔵 <b>Дополнительный гараж</b> - пригодится для размещения мото и велотехники, снегоходов, квадроциклов, катера.\n\n"
            "<i>Если в списке увлечений вашей семьи есть такие активности – дополнительный гараж может стать полезной частью вашего будущего домовладения.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "gostevayaparkovka":
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/gostp.jpg"),
            "🔵 <b>Гостевая парковка</b> - эта зона отвечает за удобство визита ваших близких и друзей.\n\n"
            "<i>Здесь важно определить, сколько машин должно поместиться на парковку для гостей и какое покрытие площадки будет оптимальным.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)


    # хандлим 54.5

    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="nazad4")
    markup.add(back)

    if call.data == "nazad4":
        handler54_5.block4_55(call.message, bot)
    
    if call.data == "besetka":
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/besedkta2.jpg"),
            "🔵 Представьте уютное место, где вы собираетесь с семьей за чашкой чая или устраиваете вечерние посиделки с друзьями.\n\n"
            "<b>Беседка</b> — не просто опция, а уголок отдыха, наполненный теплом и умиротворением. Её можно спроектировать открытой, воздушной или внесезонной, для круглогодичного использования.\n \n"
            "Летом здесь будет освежать искусственный туман, зимой – согревать живой огонь, а зона барбекю будет дразнить обоняние круглый год.\n\n"
            "<i>Эта территория точно станет вашим личным укрытием от городской суеты.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "zonaognya":
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/zonaognya.jpg"),
            "🔵 <b>Зона огня</b> - Открытый огонь на свежем воздухе всегда притягивает взгляды и дарит ощущение тепла и безопасности.\n\n"
            "Представьте вечера под уютный треск поленьев в каменном очаге, душевные беседы с близкими у современного фейерпита, смех детей, жарящих угощения возле уютной чаши для костра — вместе с ними зона огня подарит вам ощущение спокойствия и чувство настоящего дома.",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "relaxzona":
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/relazx11.jpg"),
            "🔵 Место, где можно забыть обо всём мире, отдохнуть душой и телом\n\n"
            "Это могут быть гамаки между деревьями, шезлонги у бассейна или павильон с мягкими подушками. \n\n"
            "<i>Добавим стильный текстиль, садовый фонтанчик или сад ароматов — и создадим ваш персональный оазис спокойствия.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "banyaspa":
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/banya22.jpg"),
            "🔵 <b>Ритуалы очищения и отдыха прямо у вас дома</b>\n\n"
            "Русская баня с ароматным паром, финская сауна или современный СПА-комплекс — выберите то, что подарит вам бодрость и расслабление.\n\n"
            "Важно продумать зону отдыха с купелью, комнату для чаепитий и отделку из натурального дерева.\n\n"
            "<i>Каждая процедура в приватной СПА-зоне станет маленьким праздником и источником ежедневного удовольствия и заботы о здоровье всех членов семьи.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "detskayaplashadka":
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/detskayaplashadka2.jpg"),
            "🔵 <b>Место, где рождаются счастливые воспоминания о детстве</b>\n\n"
            "Горки, качели, домики на деревьях или песочница — пусть у детей будет пространство для игр и фантазий. Важно выбрать безопасные натуральные материалы, гармоничные цвета и продумать тенистый навес. \n\n"
            "<i>А может, добавить мини-скалодром или качели для всей семьи?</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "sportivna":
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/sportivnyaa3.jpg"),
            "🔵 <b>Здоровье и энергия прямо во дворе</b>\n\n"
            "Турники, тренажеры, поле для мини-футбола или йоги — все, что вдохновляет вас на движение. \n\n"
            "<i>Можно сделать покрытие из резиновой крошки, установить освещение для вечерних тренировок и даже обустроить зону для функционального тренинга.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "gostevoydomik":
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/gostevaya3.jpg"),
            "🔵 <b>Чтобы гости чувствовали себя как дома</b>\n\n"
            "Гостевой дом дарит полную автономию вашим близким и родным и расширяет возможности вашего домовладения. Дополнительное жилое пространство позволяет владельцам сохранять приватность и привычный уклад семьи, при этом обеспечивая своим гостям максимум комфорта.\n\n"
            "<i>С такими условиями каждый визит станет в радость и гостям, и владельцам. А еще домик может использоваться, например, как рабочее пространство или место для отдыха.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    

    # хандлим 55.5

    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="nazad5")
    markup.add(back)

    if call.data == "nazad5":
        handler55_5.block4_56(call.message, bot)
    
    if call.data == "geomet":
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/geoimmettadf.jpg"),
            "🔵 <b>Строгая геометрия и чёткие линии</b>\n\n"
            "Ландшафтный дизайн с прямыми линиями выглядит элегантно и современно. Представьте аккуратные стриженые изгороди, идеальные квадраты газонов и дорожки, ведущие взгляд к фокусным точкам. \n\n"
            "Это стиль для тех, кто ценит порядок и лаконичность, где каждый элемент подчиняется общей гармонии.\n\n"
            "<i>Идеально для классических домов и ценителей строгой красоты.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "ecetest":
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/estest23.jpg"),
            "🔵 <b>Природный стиль с естественными формами</b>\n\n"
            "Двор, который выглядит так, будто его создала сама природа. Плавные линии, немного «дикие» посадки, цветущие луговые травы и извилистые тропинки.\n\n"
            "Здесь нет места жестким формам — только мягкость, свобода и ощущение единения с окружающим миром. А ещё можно добавить водоем с неровными берегами, несимметричные группы деревьев и кустарников, укромные уголки.\n\n"
            "<i>Такой участок станет уголком нетронутой гармонии.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "minimalizmastion":
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/minimum1.jpg"),
            "🔵 <b>Современный минимализм</b>\n\n"
            "Меньше — значит больше. Чистые формы, нейтральные цвета и продуманные детали создают атмосферу спокойствия и уюта. \n\n"
            "Лаконичные дорожки, монохромные растения, строгие бетонные или деревянные плоскости — такая стилизация участка не перегружает взгляд, но выглядит стильно и современно.\n\n"
            "<i>Идеально для тех, кто ценит простоту и функциональность без лишнего декора.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "mnogazeleni":
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/mnogozeleni1.jpg"),
            "🔵 <b>Максимум декоративной зелени</b>\n\n"
            "Буйство листвы, густые кроны деревьев, живые изгороди и сочные газоны — В таком пространстве участка зелень играет главную роль.\n\n"
            "Это прохлада в жаркий день, шелест листьев и ощущение свежести. \n\n"
            "<i>Добавьте вьющиеся растения на перголы, многоуровневые клумбы и тенистые уголки — и вы получите настоящий оазис, где так приятно затеряться от ежедневной суеты.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "functional":
        bot.send_photo(
            call.message.chat.id,
            InputFile("main_photo/funchional3.jpg"),
            "🔵 <b>Практичность как главное правило</b>\n\n"
            "Вам важно вписать в участок все желаемые объекты, а стиль вторичен? Тогда участок на 200% должен работать на вас! Удобные дорожки, продуманные зоны (парковка, огород, хозблок), простые в уходе растения и материалы, которые служат годами.\n\n"
            "Здесь нет места сложному декору — только то, что делает вашу жизнь комфортнее.\n\n"
            "<i>Но и в таком подходе можно создать уют, добавив пару уютных уголков для отдыха.</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
        bot.delete_message(call.message.chat.id, call.message.id)
    
    if call.data == "sadfasfasfsadfasdfasdfasfsdfasd":
        bot.delete_message(call.message.chat.id, call.message.id)
        handler311.block4_31(call.message, bot)

    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton("◀️ Назад", callback_data="sadfasfasfsadfasdfasdfasfsdfasd"))
    if call.data == "asdfasdfadffdsfsadfsadf":
        bot.send_photo(call.message.chat.id, InputFile("main_photo/igrovaya2.jpg"),
                       "<b>🔵Игровая — мир веселья и творчества</b>\n"
                       "Здесь можно разместить зоны для настольных игр, спортивный уголок или даже мини-кинотеатр. Яркие акценты, безопасные материалы\n\n"
                       "<i>Гибкая планировка помогут создать пространство, где дети будут счастливы. Давайте воплотим их мечты в реальность!</i>",
                         reply_markup=markup, parse_mode="HTML")
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "asdfasdfasdfasdf":
        bot.send_photo(call.message.chat.id, InputFile("main_photo/dlyazanathi3.jpg"),
                       "<b>🔵Комната для занятий — пространство для вдохновения и продуктивности</b>\n"
                       "Важно продумать удобный стол, эргономичное кресло и систему хранения для учебных принадлежностей\n\n"
                       "Хорошее освещение и спокойная цветовая гамма помогут сосредоточиться и быть максимально продуктивными.\n\n"
                       "<i>Это пространство, где личность вашего ребенка будет развиваться максимально гармонично!</i>",
                         reply_markup=markup, parse_mode="HTML")
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "asdfasdfasdsadasdfff":
        bot.send_photo(call.message.chat.id, InputFile("main_photo/gardetobta.jpg"),
                       "<b>🔵Гардеробная — залог порядка и системного хранения</b>\n"
                       "Встроенные системы хранения, подсветка и зеркала сделают её функциональной и стильной.\n\n"
                       "<i>Гардеробная в детской не только позволит с удобством хранить детские вещи, но и поможет вашим наследникам стать более аккуратными, системными и организованными.</i>",
                         reply_markup=markup, parse_mode="HTML")
        bot.delete_message(call.message.chat.id, call.message.id)
    if call.data == "asdfasdfsadfasdf1":
        bot.send_photo(call.message.chat.id, InputFile("main_photo/sanuzeaal.jpg"),
                       "<b>🔵Детский санузел — яркое и безопасное пространство!</b>\n"
                       "Важно выбрать удобную сантехнику, надёжную инженерию и дизайн, актуальный возрасту.\n\n"
                       "<i>Такой санузел важно сделать практичным, чтобы развивать детскую самостоятельность и автономность.</i>",
                         reply_markup=markup, parse_mode="HTML")
        bot.delete_message(call.message.chat.id, call.message.id)




    if call.data == "oneroom":
        createdb.exdb("1", 34, call.message.chat.id)
        handler31.block4_31(call.message, bot)
    if call.data == "tworooms":
        createdb.exdb("2", 34, call.message.chat.id)
        handler31.block4_31(call.message, bot)
    if call.data == "threerooms":
        createdb.exdb("3", 34, call.message.chat.id)
        handler31.block4_31(call.message, bot)
    if call.data == "thiszoneisnotneeded":
        createdb.exdb("NULL", 34, call.message.chat.id)
        handler34.block4_34(call.message, bot)
    if call.data == "bathroom_two":
        createdb.exdb("2", 41, call.message.chat.id)
        handler38_2.block4_38(call.message, bot)
    if call.data == "bathroom_three":
        createdb.exdb("3", 41, call.message.chat.id)
        handler38_3.block4_38(call.message, bot)
    if call.data == "bathroom_four_and_more":
        createdb.exdb("4", 41, call.message.chat.id)
        handler38.block4_38(call.message, bot)
    


        
    

    
    if call.data == "yes_buyed":
        createdb.exdb("Да", 68, call.message.chat.id)
        handler59.block4_40(call.message, bot)
    if call.data == "not_buyed":
        createdb.exdb("Нет", 68, call.message.chat.id)
        handler71.block4_40(call.message, bot)
    if call.data == "not_need_help":
        createdb.exdb("Нет, нужна помощь", 68, call.message.chat.id)
        handler71.block4_40(call.message, bot)
    if call.data == "very_bad":
        createdb.exdb("Подъездные пути в плохом состоянии", 73, call.message.chat.id)
        handler64.block4_46(call.message, bot)
    if call.data == "bad":
        createdb.exdb("Грунтовая дорога", 73, call.message.chat.id)
        handler64.block4_46(call.message, bot)
    if call.data == "good":
        createdb.exdb("Дорога, отсыпанная щебнем", 73, call.message.chat.id)
        handler64.block4_46(call.message, bot)
    if call.data == "very_good":
        createdb.exdb("Дорога с твёрдым покрытием", 73, call.message.chat.id)
        handler64.block4_46(call.message, bot)
    if call.data == "isnot":
        createdb.exdb("Нет", 75, call.message.chat.id)
        handler66.block4_40(call.message, bot)
    if call.data == "isyes":
        createdb.exdb("Да", 75, call.message.chat.id)
        handler67.block4_40(call.message, bot)
    if call.data == "isnotis":
        createdb.exdb("Нет", 76, call.message.chat.id)
        handler67.block4_40(call.message, bot)
    if call.data == "isnotidk":
        createdb.exdb("Не знаю", 76, call.message.chat.id)
        handler67.block4_40(call.message, bot)
    if call.data == "isyesis":
        createdb.exdb("Да", 76, call.message.chat.id)
        handler67.block4_40(call.message, bot)
    if call.data == "isnotisnot":
        createdb.exdb("Нет", 77, call.message.chat.id)
    if call.data == "isyesisyes":
        createdb.exdb("Да", 77, call.message.chat.id)
        handler68_5.block4_40(call.message, bot)


    if call.data == "notisnotisnot":
        createdb.exdb("Нет", 78, call.message.chat.id)
        handler68_5.block4_40(call.message, bot)


    # хандлим 731

    markup = InlineKeyboardMarkup(row_width=1)
    back = InlineKeyboardButton("◀️ Назад", callback_data="nazad6")
    markup.add(back)




    if call.data == "yesisyesisyes":
        createdb.exdb("Да", 78, call.message.chat.id)
        handler68_5.block4_40(call.message, bot)

    if call.data == "notisnotisnotasd":
        createdb.exdb("Нет", 78, call.message.chat.id)
        handler69.block4_46(call.message, bot)
    if call.data == "yesisyesisyesasd":
        createdb.exdb("Да", 78, call.message.chat.id)
        handler69.block4_46(call.message, bot)



    if call.data == "tochno":
        createdb.exdb("Точность и расчёт", 83, call.message.chat.id)
        handler73_5.block4_40_1(call.message, bot)
        messages = cache73.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)


    if call.data == "idealno":
        createdb.exdb("Идеальное соответствие ожиданиям", 83, call.message.chat.id)
        handler73_5.block4_40_1(call.message, bot)
        messages = cache73.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)


    if call.data == "optimi":
        createdb.exdb("Оптимальность строительства", 83, call.message.chat.id)
        handler73_5.block4_40_1(call.message, bot)
        messages = cache73.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)


    if call.data == "safety":
        createdb.exdb("Безопасность работы", 83, call.message.chat.id)
        handler73_5.block4_40_1(call.message, bot)
        messages = cache73.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)


    if call.data == "personal":
        createdb.exdb("Персональный подход", 83, call.message.chat.id)
        handler73_5.block4_40_1(call.message, bot)
        messages = cache73.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)

    
    if call.data == "optimal":
        createdb.exdb("Оптимальный баланс", 85, call.message.chat.id)
        messages = cache74.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)
        cache74.pop(call.message.chat.id)
        handler75.block4_40(call.message, bot)
    if call.data == "bigstandart":
        bot.delete_message(call.message.chat.id, call.message.id)
        createdb.exdb("Высокий стандарт", 85, call.message.chat.id)
        messages = cache74.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)
        cache74.pop(call.message.chat.id)
        handler75.block4_40(call.message, bot)
        
    if call.data == "controlzatrat":
        bot.delete_message(call.message.chat.id, call.message.id)
        createdb.exdb("Контроль затрат", 85, call.message.chat.id)
        messages = cache74.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)
        cache74.pop(call.message.chat.id)
        handler75.block4_40(call.message, bot)
        
    if call.data == "familybuild":
        bot.delete_message(call.message.chat.id, call.message.id)
        createdb.exdb("Семейный оплот", 85, call.message.chat.id)
        messages = cache74.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)
        cache74.pop(call.message.chat.id)
        handler75.block4_40(call.message, bot)

    if call.data == "asdanazasdasd":
        handler51_5.block4_52(call.message, bot)

    if call.data == "vinnaya":
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(InlineKeyboardButton("◀️ Назад", callback_data="asdanazasdasd"))
        bot.delete_message(call.message.chat.id, call.message.id)
        media = [InputMediaPhoto(open("main_photo/barasdasd.jpg", "rb")), 
                 InputMediaPhoto(open("main_photo/callyanyana.jpg", "rb")), 
                 InputMediaPhoto(open("main_photo/sigarnaya.jpg", "rb"))
        ] 
        data = bot.send_media_group(call.message.chat.id, media)
        cache551[call.message.chat.id] = data
        bot.send_message(call.message.chat.id,
                        "🔵 <b>Ваш личный уголок для релакса и атмосферных вечеров</b>\n\n"
                         "<i>Продумайте: будет ли это стильный лаунж с коллекцией виски, восточная кальянная с низкими диванами или классическая сигарная комната с дубовыми панелями?</i>",
                         parse_mode="HTML", reply_markup=markup)
    if call.data == "oruheynaya":
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(InlineKeyboardButton("◀️ Назад", callback_data="asdanazasdasd"))
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id, InputFile("main_photo/orujeyna.jpg"),
                        "<b>🔵Брутальная территория статуса</b>\n\n"
                         "<i>Важно продумать его до мелочей: система вентиляции, освещение витрин, уровень безопасности.\n\nА главное – удобство для демонстрации трофеев гостям. </i>",
                         parse_mode="HTML", reply_markup=markup)
    if call.data == "seyfovata":
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(InlineKeyboardButton("◀️ Назад", callback_data="asdanazasdasd"))
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/safe.jpg"),
            "🔵 <b>Когда надёжность – в системе ваших ценностей</b>\n\n"
            "<i>Решите: скрытый за картиной сейф, отдельная комната с биометрикой или стилизованный «банковский» блок в интерьере?</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "tropheynaya":
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(InlineKeyboardButton("◀️ Назад", callback_data="asdanazasdasd"))
        media = [InputMediaPhoto(open("main_photo/trof.jpg", "rb")), 
                 InputMediaPhoto(open("main_photo/mudzei.jpg", "rb")), 
                 InputMediaPhoto(open("main_photo/galerrey.jpg", "rb"))
        ] 
        data = bot.send_media_group(call.message.chat.id, media)
        cache551[call.message.chat.id] = data
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, 
                       "<b>🔵 Достойное обрамление ваших достижений</b>\n\n Нужны ли витрины с подсветкой, ротационные стенды или пространство для будущих экспонатов?\n\n <i>Ваша коллекция нуждается в безупречной оправе!</i>", parse_mode="HTML", reply_markup=markup)
    if call.data == "SPAzonavnutri":
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(InlineKeyboardButton("◀️ Назад", callback_data="asdanazasdasd"))
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(call.message.chat.id,InputFile("main_photo/spa.png"), "<b>🔵 Ваш персональный курорт прямо дома</b>\n\n Будет это лазурная гладь бассейна с панорамным окном?\n\n Хамам с мозаикой и массажным столом?\n\n Джакузи, где так здорово расслабиться после долгого и продуктивного дня?\n\n Или душистая кедровая баня с сауной, парной и купелью?", parse_mode="HTML", reply_markup=markup)
    if call.data == "sportivnaytazona":
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(InlineKeyboardButton("◀️ Назад", callback_data="asdanazasdasd"))
        media = [InputMediaPhoto(open("main_photo/sport.jpg", "rb")), 
                 InputMediaPhoto(open("main_photo/billyard.jpg", "rb")), 
                 InputMediaPhoto(open("main_photo/gamezone.jpg", "rb"))
        ] 
        data = bot.send_media_group(call.message.chat.id, media)
        cache551[call.message.chat.id] = data
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(
            call.message.chat.id,
            "🔵 <b>Территория азарта и движения</b>\n\n"
            "Выбирайте, что больше по душе: тренажёры с видом на сад, бильярдный стол с баром или игровая с приставками для непревзойдённых каток?\n\n"
            "<i>Создайте условия для макисмального наслаждения и процессом, и победами!</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "kinozal":
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(InlineKeyboardButton("◀️ Назад", callback_data="asdanazasdasd"))
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id,InputFile("main_photo/kino.jpg"),
            "🔵 <b>Оскар в студию!</b>\n\n"
            "Что важно для вас: безупречная акустика, кресла с подогревом, потолок «звёздное небо» или классический кинематографичный дизайн?\n\n"
            "<i>В такой атмосфере эмоции от кино особенно яркие!</i>",
            parse_mode="HTML",
            reply_markup=markup
        )
    if call.data == "privatnaya":
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(InlineKeyboardButton("◀️ Назад", callback_data="asdanazasdasd"))
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_photo(
            call.message.chat.id, InputFile("main_photo/priv.jpg"),
            "🔵 <b>Интерьер, где слова излишни</b>\n\n"
            "<i>Деликатно обсудим детали: звукоизоляция, скрытое освещение, трансформируемая мебель или антикварная кровать с балдахином?</i>",
            parse_mode="HTML",
            reply_markup=markup
        )



    if call.data == "sootvetstvieplanu":
        createdb.exdb("Соответствие плану", 87, call.message.chat.id)
        block4_40(call.message, bot)
        messages = cache75.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)
    if call.data == "realisegoals":
        createdb.exdb("Новое качество жизни", 87, call.message.chat.id)
        block4_40(call.message, bot)
        messages = cache75.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)
    if call.data == "miniriskiofbuild":
        createdb.exdb("Минимизировать риски стройки", 87, call.message.chat.id)
        block4_40(call.message, bot)
        messages = cache75.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)
    if call.data == "emotionofnewhouse":
        createdb.exdb("Эмоции от нового дома", 87, call.message.chat.id)
        block4_40(call.message, bot)
        messages = cache75.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)
    if call.data == "newqualityoflife":
        createdb.exdb("Новый опыт", 87, call.message.chat.id)
        block4_40(call.message, bot)
        messages = cache75.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)

    if call.data == "nasdfklasjfsadfasdfd":
        infohandler11.infoblock10_5(call.message, bot)

    if call.data == "planirivkauchastka":
        bot.delete_message(call.message.chat.id, call.message.id)
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(InlineKeyboardButton("◀️ Назад", callback_data="nasdfklasjfsadfasdfd"))
        media = [InputMediaPhoto(open("main_photo/bezplanirovki.jpg", "rb")), InputMediaPhoto(open("main_photo/splanirovkoy.jpg", "rb"))]
        data = bot.send_media_group(call.message.chat.id, media)
        cache5551[call.message.chat.id] = data
        bot.send_message(parse_mode="HTML",
                         text="<b>🔵 Уже выбрали участок для будущего дома или пока в поисках?</b>\n\n"
                              "Одновременно с проектом дома команда архитекторов, конструкторов, генпланистов и прорабов строительной компании IVAN DOM Rostov выполнит для вас предварительную планировку участка.\n\n"
                              "Если вы сейчас в процессе подбора, предпланировка поможет вам получить максимум информации о планируемой покупке. \n\n"
                              "В её основе – точные факты, выводы, знания и опыт нашего собственного проектного отдела. Так вы сделаете лучший выбор и оградите себя от неудачных вложений.\n\n"
                              "Предпланировка поможет:\n\n"
                              "🔹Рационально использовать все возможности пространства\n"
                              "🔹Обеспечить высокий комфорт проживания в домовладении\n"
                              "🔹Проанализировать все возможные варианты использования земельного участка\n\n"
                              "<b>Эта услуга – бонус для клиентов IVAN DOM Rostov, которые находятся на этапе выбора участка. \n\n</b>"
                              "<i>Вместе мы выберем самые оптимальные решения именно для вашего дома!</i>",
                         reply_markup=markup,
                         chat_id=call.message.chat.id)


    if call.data == "pppioiipiasdfadf":
        createdb.exdb("Не нужно доп комнат", 35, call.message.chat.id)
        handler32.block4_32(call.message, bot)
    if call.data == "zonanenuhasjhd":
        createdb.exdb("Зона не нужна", 51, call.message.chat.id)
        handler47.block4_40(call.message, bot)
    if call.data == "zonasdflkasljdfklasjf":
        createdb.exdb("Зона не нужна", 58, call.message.chat.id)
        handler53.block4_53(call.message, bot)
    if call.data == "asdfasfzonaasdfadsf":
        createdb.exdb("Зона не нужна", 64, call.message.chat.id)
        handler54_5.block4_55(call.message, bot)
    if call.data == "gotovkstroyke":
        createdb.exdb("Готов к стройке", 80, call.message.chat.id)
        handler711.block4_40(call.message, bot)
    if call.data == "asdfasfzonaaasassdfadsf":
        createdb.exdb("Ничего не нужно", 66, call.message.chat.id)
        handler56.block4_56(call.message, bot)
    if call.data == "nothing_first":
        createdb.exdb("Ничего не нужно", 17, call.message.chat.id)
        handler16.block4_11(call.message, bot)



    if call.data.startswith("continue"):
        calldata = call.data.split("_")
        if call.data.split("_")[1] == str(4):
            if len(calldata) == 3:
                # пишем разделение данных

                converted = {
                    "0": "Создать комфорт для семьи",
                    "1": "Реализовать давнюю мечту",
                    "2": "Увеличить пространство для жизни",
                    "3": "Повысить качество жизни",
                    "4": "Рационально использовать бюджет",
                    "5": "Обеспечить надёжность дома на годы"
                }

                calldata_list = calldata[2].split(",")
                # расшифровка (работает только с этим вариантом)
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list) # используем % как разделение между строками что бы не сломать систему сохранение в временую датабазу

                createdb.exdb(updatedcalldata, 4, call.message.chat.id)
                handler5.block4_5(call.message, bot)

        elif call.data.split("_")[1] == str(5):
            if len(calldata) == 3:
            # пишем разделение данных

                converted = {
                "0": "Выразить себя в дизайне и архитектуре",
                "1": "Создать дом c wow-эффектом",
                "2": "Создать пространство для отдыха",
                "3": "Дом, удобный в эксплуатации",
                "4": "Дом с возможностью модернизации",
                "5": "Жизнь по моим правилам"
            }

                calldata_list = calldata[2].split(",")
                # разшифровка (работает только с этим вариантом)
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list) # используем % как разделение между строками что бы не сломать систему сохранение в временую датабазу

                createdb.exdb(updatedcalldata, 5, call.message.chat.id)
                handler600.block4_6(call.message, bot)
        elif call.data.split("_")[1] == str(7):
            if len(calldata) == 3:
            # пишем разделение данных

                converted = {
                "0": "Владелец дома",
                "1": "Владелица дома",
                "2": "Ребёнок/дети",
                "3": "Родители владельцев",
                "4": "Будущие внуки и правнуки",
                "5": "Периодические гости",
                "6": "Любимый питомец",
            }

                calldata_list = calldata[2].split(",")
                # разшифровка (работает только с этим вариантом)
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list) # используем % как разделение между строками что бы не сломать систему сохранение в временую датабазу

                createdb.exdb(updatedcalldata, 9, call.message.chat.id)
                handler8.block4_8(call.message, bot)
        elif call.data.split("_")[1] == str(21):
            if len(calldata) == 3:
                converted = {
                    "0": "Прихожая",
                    "1": "Гардеробная",
                    "2": "Санузел",
                    "3": "Лапомойка"
                }

                calldata_list = calldata[2].split(",")
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list)

                createdb.exdb(updatedcalldata, 23, call.message.chat.id)

                handler22.block4_11(call.message, bot)
        elif call.data.split("_")[1] == str(23):
            if len(calldata) == 3:
                converted = {
                    "0": "Объединить кухню с гостиной",
                    "1": "Разделить кухню с гостиной",
                    "2": "Частично объединить",
                    "3": "Соединить гостиную с террасой"
                }

                calldata_list = calldata[2].split(",")
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list)

                createdb.exdb(updatedcalldata, 26, call.message.chat.id)

                handler24.block4_24(call.message, bot)

        elif call.data.split("_")[1] == str(27):
            if len(calldata) == 3:
                converted = {
                    "0": "Спальня",
                    "1": "Отдельный санузел",
                    "2": "Гардеробная",
                    "3": "Приватная терраса"
                }

                calldata_list = calldata[2].split(",")
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list)
                createdb.exdb(updatedcalldata, 31, call.message.chat.id)
                handler28.block4_28(call.message, bot)
        elif call.data.split("_")[1] == str(31):
            if len(calldata) == 3:
                converted = {
                    "0": "Игровая комната",
                    "1": "Комната для занятий",
                    "2": "Гардеробная",
                    "3": "Детский санузел"
                }

                calldata_list = calldata[2].split(",")
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list)

                createdb.exdb(updatedcalldata, 35, call.message.chat.id)
                handler32.block4_32(call.message, bot)
        elif call.data.split("_")[1] == str(34):
            if len(calldata) == 3:
                converted = {
                    "0": "Одна гостевая",
                    "1": "Две гостевые",
                    "2": "Дополнительный санузел"
                }

                calldata_list = calldata[2].split(",")
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list)

                createdb.exdb(updatedcalldata, 38, call.message.chat.id)

                handler35.block4_32(call.message, bot)
        elif call.data.split("_")[1] == str(39):
            if len(calldata) == 3:
                converted = {
                    "0": "Ванна",
                    "1": "Душ",
                    "2": "Тропический душ",
                    "3": "Раковина",
                    "4": "Двойная раковина",
                    "5": "Унитаз",
                    "6": "Биде",
                    "7": "Гигиенический душ"
                }

                calldata_list = calldata[2].split(",")
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list)
                createdb.exdb(updatedcalldata, 43, call.message.chat.id)
                handler40.block4_40(call.message, bot)
        elif call.data.split("_")[1] == str(392):
            if len(calldata) == 3:
                converted = {
                    "0": "Ванна",
                    "1": "Душ",
                    "2": "Тропический душ",
                    "3": "Раковина",
                    "4": "Двойная раковина",
                    "5": "Унитаз",
                    "6": "Биде",
                    "7": "Гигиенический душ"
                }

                calldata_list = calldata[2].split(",")
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list)
                createdb.exdb(updatedcalldata, 43, call.message.chat.id)
                handler402.block4_40(call.message, bot)
        elif call.data.split("_")[1] == str(41):
            if len(calldata) == 3:
                converted = {
                    "0": "Ванна",
                    "1": "Душ",
                    "2": "Тропический душ",
                    "3": "Раковина",
                    "4": "Двойная раковина",
                    "5": "Унитаз",
                    "6": "Биде",
                    "7": "Гигиенический душ"
                }

                calldata_list = calldata[2].split(",")
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list)
                createdb.exdb(updatedcalldata, 45, call.message.chat.id)
                handler42.block4_40(call.message, bot)
        elif call.data.split("_")[1] == str(413):
            if len(calldata) == 3:
                converted = {
                    "0": "Ванна",
                    "1": "Душ",
                    "2": "Тропический душ",
                    "3": "Раковина",
                    "4": "Двойная раковина",
                    "5": "Унитаз",
                    "6": "Биде",
                    "7": "Гигиенический душ"
                }

                calldata_list = calldata[2].split(",")
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list)
                createdb.exdb(updatedcalldata, 45, call.message.chat.id)
                handler42_3.block4_40(call.message, bot)
        elif call.data.split("_")[1] == str(43):
            if len(calldata) == 3:
                converted = {
                    "0": "Ванна",
                    "1": "Душ",
                    "2": "Тропический душ",
                    "3": "Раковина",
                    "4": "Двойная раковина",
                    "5": "Унитаз",
                    "6": "Биде",
                    "7": "Гигиенический душ"
                }

                calldata_list = calldata[2].split(",")
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list)
                createdb.exdb(updatedcalldata, 47, call.message.chat.id)
                handler44.block4_40(call.message, bot)
        elif call.data.split("_")[1] == str(445):
            if len(calldata) == 3:
                converted = {
                    "0": "Ванна",
                    "1": "Душ",
                    "2": "Тропический душ",
                    "3": "Раковина",
                    "4": "Двойная раковина",
                    "5": "Унитаз",
                    "6": "Биде",
                    "7": "Гигиенический душ"
                }

                calldata_list = calldata[2].split(",")
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list)
                createdb.exdb(updatedcalldata, 49, call.message.chat.id)
                handler45.block4_40(call.message, bot)
        elif call.data.split("_")[1] == str(46):
            if len(calldata) == 3:

                converted = {
                    "0": "Кабинет",
                    "1": "Мастерская",
                    "2": "Библиотека"
                }

                calldata_list = calldata[2].split(",")
                # расшифровка (работает только с этим вариантом)
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list) # используем % как разделение между строками что бы не сломать систему сохранение во временую датабазу
                
                createdb.exdb(updatedcalldata, 51, call.message.chat.id)
                handler47.block4_40(call.message, bot)
        elif call.data.split("_")[1] == str(48):
            if len(calldata) == 3:
            # пишем разделение данных

                converted = {
                    "0": "Прачечная",
                    "1": "Кладовая",
                    "2": "Серверная",
                    "3": "Комната для персонала",
                    "4": "Инженерная",
                    "5": "Котельная",
                    "6": "Хозблок"
                }

                calldata_list = calldata[2].split(",")
                # разшифровка (работает только с этим вариантом)
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list) # используем % как разделение между строками что бы не сломать систему сохранение в временую датабазу

                createdb.exdb(updatedcalldata, 54, call.message.chat.id)
                handler49.block4_40(call.message, bot)
        elif call.data.split("_")[1] == str(52):
            if len(calldata) == 3:
            # пишем разделение данных

                converted = {
                    "0": "Бар / Кальянная/ Сигарная",
                    "1": "Оружейная",
                    "2": "Сейфовая",
                    "3": "Трофейная/ Музей/ Галерея",
                    "4": "Бассейн/СПА в доме",
                    "5": "Спорт-зона/ Бильярд/ Гейм-зона",
                    "6": "Кинозал",
                    "7": "Приватная комната для взрослых"

                }

                calldata_list = calldata[2].split(",")
                # разшифровка (работает только с этим вариантом)
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list) # используем % как разделение между строками чтобы не сломать систему сохранение во временую датабазу

                createdb.exdb(updatedcalldata, 58, call.message.chat.id)
                handler53.block4_53(call.message, bot)
        elif call.data.split("_")[1] == str(54):
            if len(calldata) == 3:
            # пишем разделение данных

                converted = {
                    "0": "Терраса у дома",
                    "1": "Крыльцо",
                    "2": "Навес для авто, примыкающий к дому",
                    "3": "Навес для авто отдельностоящий",
                    "4": "Гараж, примыкающий к дому",
                    "5": "Гараж отдельностоящий",
                    "6": "Доп. гараж",
                    "7": "Гостевая парковка",
                }

                calldata_list = calldata[2].split(",")
                # разшифровка (работает только с этим вариантом)
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list) # используем % как разделение между строками что бы не сломать систему сохранение в временую датабазу

                createdb.exdb(updatedcalldata, 64, call.message.chat.id)
                handler55.block4_55(call.message, bot)
        elif call.data.split("_")[1] == str(55):
            if len(calldata) == 3:
            # пишем разделение данных

                converted = {
                    "0": "Беседка — Открытая беседка",
                    "1": "Зона огня",
                    "2": "Релакс-зона",
                    "3": "Баня / СПА",
                    "4": "Детская площадка",
                    "5": "Спортивная площадка",
                    "6": "Гостевой домик"
                }

                calldata_list = calldata[2].split(",")
                # разшифровка (работает только с этим вариантом)
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list) # используем % как разделение между строками что бы не сломать систему сохранение в временую датабазу

                createdb.exdb(updatedcalldata, 65, call.message.chat.id)
                handler56.block4_56(call.message, bot)
        elif call.data.split("_")[1] == str(56):
            if len(calldata) == 3:
            # # пишем разделение данных

                converted = {
                    "0": "Геометричность",
                    "1": "Естественность",
                    "2": "Минимализм",
                    "3": "Много зелени",
                    "4": "Функционал важнее стиля",
                }

                calldata_list = calldata[2].split(",")
                # разшифровка (работает только с этим вариантом)
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list) # используем % как разделение между строками что бы не сломать систему сохранение в временую датабазу

                createdb.exdb(updatedcalldata, 66, call.message.chat.id)
                handler57.block4_57(call.message, bot)
        elif call.data.split("_")[1] == str(65):
            if len(calldata) == 3:
            # # пишем разделение данных

                converted = {
                    "0": "Вода",
                    "1": "Электроэнергия",
                    "2": "Газ",
                    "3": "Канализация",
                    "4": "Высокоскоростной интернет"
                }

                calldata_list = calldata[2].split(",")
                # разшифровка (работает только с этим вариантом)
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list) # используем % как разделение между строками что бы не сломать систему сохранение в временую датабазу

                createdb.exdb(updatedcalldata, 74, call.message.chat.id)
                handler65.block4_40(call.message, bot)
        elif call.data.split("_")[1] == str(70):
            if len(calldata) == 3:
            # пишем разделение данных

                converted = {
                    "0": "Снос строений",
                    "1": "Спил и корчевание деревьев",
                    "2": "Пересадка растений",
                    "3": "Уборка мусора",
                    "4": "Земляные работы",
                    "5": "Монтаж подпорных стенок",
                    "6": "Оградить участок"
                }

                calldata_list = calldata[2].split(",")
                # разшифровка (работает только с этим вариантом)
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list) # используем % как разделение между строками что бы не сломать систему сохранение в временую датабазу
                createdb.exdb(updatedcalldata, 79, call.message.chat.id)
                handler711.block4_40(call.message, bot)
        elif call.data.split("_")[1] == str(151):
            if len(calldata) == 3:
            # пишем разделение данных

                converted = {
                    "0": "Панорамные окна",
                    "1": "Второй свет",
                    "2": "Плоская кровля с зоной отдыха",
                    "3": "Эркер",
                    "4": "Атриум",
                    "5": "Балкон",
                    "6": "Подвал"
                }

                calldata_list = calldata[2].split(",")
                # разшифровка (работает только с этим вариантом)
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list) # используем % как разделение между строками что бы не сломать систему сохранение в временую датабазу

                createdb.exdb(updatedcalldata, 17, call.message.chat.id)
                handler16.block4_11(call.message, bot)
        elif call.data.split("_")[1] == str(171):
            if len(calldata) == 3:
            # пишем разделение данных

                converted = {
                    "0": "Кирпич керамический",
                    "1": "Кирпич ручной формовки",
                    "2": "Ригель ручной формовки",
                    "3": "Декоративная штукатурка",
                    "4": "Натуральное дерево",
                    "5": "Природный камень",
                    "6": "Фасадные панели",
                    "7": "Гибкая керамика"
                }

                calldata_list = calldata[2].split(",")
                # разшифровка (работает только с этим вариантом)
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list) # используем % как разделение между строками что бы не сломать систему сохранение в временую датабазу

                createdb.exdb(updatedcalldata, 19, call.message.chat.id)
                handler18.block4_11(call.message, bot)
        elif call.data.split("_")[1] == str(191):
            if len(calldata) == 3:
            # пишем разделение данных

                converted = {
                    "0": "Металлочерепица",
                    "1": "Цементно-песчаная черепица",
                    "2": "Керамика",
                    "3": "Гибкая битумная черепица",
                    "4": "Композитная черепица",
                    "5": "Фальцевая кровля",
                    "6": "Плоская неэксплуатируемая кровля",
                    "7": "Плоская эксплуатируемая кровля",
                }

                calldata_list = calldata[2].split(",")
                # разшифровка (работает только с этим вариантом)
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list) # используем % как разделение между строками что бы не сломать систему сохранение в временую датабазу

                createdb.exdb(updatedcalldata, 21, call.message.chat.id)
                handler20.block4_11(call.message, bot)
        elif call.data.split("_")[1] == str(464):
            if len(calldata) == 3:
            # пишем разделение данных

                converted = {
                    "0": "Образ дома отражает мой стиль и вкус",
                    "1": "Тишина и уединение, спокойствие",
                    "2": "Приватность каждого члена семьи",
                    "3": "Эргономика: дом удобен для жизни",
                    "4": "Много вариантов досуга с семьёй",
                    "5": "Практичность и функционал планировок",
                    "6": "Энергоэффективность и экологичность",
                    "7": "Безопасность, технологичность",
                }

                calldata_list = calldata[2].split(",")
                # разшифровка (работает только с этим вариантом)
                for i in range(len(calldata_list)):
                    item = calldata_list[i]
                    data = converted.get(item)
                    calldata_list[i] = str(data) if data is not None else ""
                    updatedcalldata = "%".join(calldata_list) # используем % как разделение между строками что бы не сломать систему сохранение в временую датабазу

                createdb.exdb(updatedcalldata, 7, call.message.chat.id)
                handler6.block4_6(call.message, bot)
        if call.data == "continue_14":
            handler13_1.block4_13_1(call.message, bot)
        if call.data == "continue_16":
            handler15_1.block15_1(call.message, bot)
        if call.data == "continue_18":
            handler17_1.block17_1(call.message, bot)
        if call.data == "continue_20":
            handler19_1.block4_9(call.message, bot)
        if call.data == "continue_63":
            handler10.block4_10(call.message, bot)
        if call.data == "continue_90":
            handler21.block4_21(call.message, bot)
        if call.data == "continue_121":
            handler13_1.block4_13_1(call.message, bot)
        if call.data == "continue_110":
            infohandler11.infoblock10_5(call.message, bot)
        if call.data == "continue_111":
            handler54.block4_54(call.message, bot)
        if call.data == "continue_11221":
            handler58.block4_40(call.message, bot)
        if call.data == "continue_215":
            handler21.block4_21(call.message, bot)
        if call.data == "continue_235":
            handler23.block4_23(call.message, bot)
        if call.data == "continue_455":
            handler46.block4_46(call.message, bot)
        if call.data == "continue_535":
            handler54.block4_54(call.message, bot)
        if call.data == "continue_565":
            handler55.block4_55(call.message, bot)
        if call.data == "continue_575":
            handler56.block4_56(call.message, bot)
        if call.data == "continue_731":
            handler73_5.block4_40_1(call.message, bot)
        if call.data == "continue_143":
            handler73.block4_40(call.message, bot)
        if call.data == "continue_4111":
            handler1.block4_1(call.message, bot)
        if call.data == "continue_522":
            handler52.block4_52(call.message, bot)
        if call.data == "continue_9099":
            handler11.block4_11(call.message, bot)
        if call.data == "continue_23333":
            handler233.block4_11(call.message, bot)
            messages = cache233.get(call.message.chat.id, [])
            for msg in messages:
                bot.delete_message(call.message.chat.id, msg.message_id)
        if call.data == "continue_24333":
            handler24_5.block4_24(call.message, bot)
            messages = cache245.get(call.message.chat.id, [])
            for msg in messages:
                bot.delete_message(call.message.chat.id, msg.message_id)
        if call.data == "continue_25333":
            handler25.block4_25(call.message, bot)
            messages = cache25.get(call.message.chat.id, [])
            for msg in messages:
                bot.delete_message(call.message.chat.id, msg.message_id)
        if call.data == "continue_26333":
            handler26.block4_26(call.message, bot)
            messages = cache26.get(call.message.chat.id, [])
            for msg in messages:
                bot.delete_message(call.message.chat.id, msg.message_id)
        if call.data == "continue_33333":
            handler33.block4_32(call.message, bot)
            messages = cache33.get(call.message.chat.id, [])
            for msg in messages:
                bot.delete_message(call.message.chat.id, msg.message_id)
        if call.data == "continue_333333":
            handler37.block4_37(call.message, bot)
            messages = cache37.get(call.message.chat.id, [])
            for msg in messages:
                bot.delete_message(call.message.chat.id, msg.message_id)
        if call.data == "continue_41111":
            handler11.block4_11(call.message, bot)
        if call.data == "continue_513333":
            handler51.block4_40(call.message, bot)
            messages = cache51.get(call.message.chat.id, [])
            for msg in messages:
                bot.delete_message(call.message.chat.id, msg.message_id)
        if call.data == "continue_31":
            handler31.block4_31(call.message, bot)
            


    if call.data.startswith("variant"):

        data = call.data.split("_")[1]
        number = call.data.split("_")[2]
        status = call.data.split("_")[3]
        handler = call.data.split("_")[4]
        if handler == str(4):

            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            converted = {
                    "1": "Создать комфорт для семьи",
                    "2": "Реализовать давнюю мечту",
                    "3": "Увеличить пространство для жизни",
                    "4": "Повысить качество жизни",
                    "5": "Рационально использовать бюджет",
                    "6": "Обеспечить надёжность дома на годы"
                }
            for i in range(0, 6):
                data = converted.get(str(i+1), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_4_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_3")
            

            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)


        elif handler == str(464):
            converted = {
                    "1": "Образ дома отражает мой стиль и вкус",
                    "2": "Тишина и уединение, спокойствие",
                    "3": "Приватность каждого члена семьи",
                    "4": "Эргономика: дом удобен для жизни",
                    "5": "Много вариантов досуга с семьёй",
                    "6": "Практичность и функционал планировок",
                    "7": "Энергоэффективность и экологичность",
                    "8": "Безопасность, технологичность",
                }
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            for i in range(0, 8):
                data = converted.get(str(i+1), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_"+handler+"_"+updated_status))
            # добавляем кнопки ◀️ Назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_464")
            

            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)

        elif handler == str(5):
            converted = {
                "1": "Выразить себя в дизайне и архитектуре",
                "2": "Создать дом c wow-эффектом",
                "3": "Создать пространство для отдыха",
                "4": "Дом, удобный в эксплуатации",
                "5": "Дом с возможностью модернизации",
                "6": "Жизнь по моим правилам"
            }
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            for i in range(0, 6):
                data = converted.get(str(i+1), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_"+handler+"_"+updated_status))
            # добавляем кнопки ◀️ Назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_4")
            

            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(7):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else [] 

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)
            converted = {
                "1": "Владелец дома",
                "2": "Владелица дома",
                "3": "Ребёнок/дети",
                "4": "Родители владельцев",
                "5": "Будущие внуки и правнуки",
                "6": "Периодические гости",
                "7": "Любимый питомец",
            }
            for i in range(0, 7):
                text = converted.get(str(i+1), "Неизвестный вариант")
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=(f"continue_{handler}_"+updated_status))
            # добавляем кнопки ◀️ Назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_6")
            

            markup.add(continueButton, backButton)
            

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(21):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            converted = {
                    "0": "Прихожая",
                    "1": "Гардеробная",
                    "2": "Санузел",
                    "3": "Лапомойка"
                }
            for i in range(0, 4):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=(f"continue_{handler}_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_20")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(23):
            markup = InlineKeyboardMarkup(row_width=1)
            converted = {
                "0": "Объединить кухню с гостиной",
                "1": "Разделить кухню с гостиной",
                "2": "Частично объединить",
                "3": "Соединить гостиную с террасой"
            }
            new_status = status.split(",") if status else []
            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)
            updated_status = ",".join(new_status)
            for i in range(0, 4):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=(f"continue_{handler}_"+updated_status))
            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_221")
            markup.add(continueButton, backButton)
            try:
                bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
            except Exception as e:
                if "message is not modified" not in str(e):
                    raise e
        elif handler == str(27):
            markup = InlineKeyboardMarkup(row_width=1)
            converted = {
                "0": "Спальня",
                "1": "Отдельный санузел",
                "2": "Гардеробная",
                "3": "Приватная терраса"
            }
            new_status = status.split(",") if status else []
            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)
            updated_status = ",".join(new_status)
            for i in range(0, 4):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=(f"continue_{handler}_"+updated_status))
            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_225")
            markup.add(continueButton, backButton)
            try:
                bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
            except Exception as e:
                if "message is not modified" not in str(e):
                    raise e
        elif handler == str(31):
            markup = InlineKeyboardMarkup(row_width=1)
            converted = {
                "0": "Игровая комната",
                "1": "Комната для занятий",
                "2": "Гардеробная",
                "3": "Детский санузел"
            }
            new_status = status.split(",") if status else []
            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)
            updated_status = ",".join(new_status)
            for i in range(0, 4):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=(f"continue_{handler}_"+updated_status))
            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_30")
            markup.add(continueButton, backButton)
            try:
                bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
            except Exception as e:
                if "message is not modified" not in str(e):
                    raise e
        elif handler == str(34):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            converted = {
                "0": "Одна гостевая",
                "1": "Две гостевые",
                "2": "Дополнительный санузел"
            }
            for i in range(0, 3):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_34_"+updated_status))
            # добавляем кнопки ◀️ Назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_33")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(39):
            markup = InlineKeyboardMarkup(row_width=1)

            converted = {
                    "0": "Ванна",
                    "1": "Душ",
                    "2": "Тропический душ",
                    "3": "Раковина",
                    "4": "Двойная раковина",
                    "5": "Унитаз",
                    "6": "Биде",
                    "7": "Гигиенический душ",

                }
            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            for i in range(0, 8):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_39_"+updated_status))
            # добавляем кнопки ◀️ Назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_37")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(393):
            markup = InlineKeyboardMarkup(row_width=1)

            converted = {
                    "0": "Ванна",
                    "1": "Душ",
                    "2": "Тропический душ",
                    "3": "Раковина",
                    "4": "Двойная раковина",
                    "5": "Унитаз",
                    "6": "Биде",
                    "7": "Гигиенический душ",

                }
            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            for i in range(0, 8):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_39_"+updated_status))
            # добавляем кнопки ◀️ Назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_37")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(392):
            markup = InlineKeyboardMarkup(row_width=1)

            converted = {
                    "0": "Ванна",
                    "1": "Душ",
                    "2": "Тропический душ",
                    "3": "Раковина",
                    "4": "Двойная раковина",
                    "5": "Унитаз",
                    "6": "Биде",
                    "7": "Гигиенический душ",

                }
            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            for i in range(0, 8):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_392_"+updated_status))
            # добавляем кнопки ◀️ Назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_37")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(41):
            markup = InlineKeyboardMarkup(row_width=1)

            converted = {
                    "0": "Ванна",
                    "1": "Душ",
                    "2": "Тропический душ",
                    "3": "Раковина",
                    "4": "Двойная раковина",
                    "5": "Унитаз",
                    "6": "Биде",
                    "7": "Гигиенический душ",

                }
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            for i in range(0, 8):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_41_"+updated_status))
            # добавляем кнопки ◀️ Назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_37")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(413):
            markup = InlineKeyboardMarkup(row_width=1)

            converted = {
                    "0": "Ванна",
                    "1": "Душ",
                    "2": "Тропический душ",
                    "3": "Раковина",
                    "4": "Двойная раковина",
                    "5": "Унитаз",
                    "6": "Биде",
                    "7": "Гигиенический душ",

                }
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            for i in range(0, 8):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_413_"+updated_status))
            # добавляем кнопки ◀️ Назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_37")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(43):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            converted = {
                    "0": "Ванна",
                    "1": "Душ",
                    "2": "Тропический душ",
                    "3": "Раковина",
                    "4": "Двойная раковина",
                    "5": "Унитаз",
                    "6": "Биде",
                    "7": "Гигиенический душ",
                }
            for i in range(0, 8):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_43_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_37")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(43):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            converted = {
                    "0": "Ванна",
                    "1": "Душ",
                    "2": "Тропический душ",
                    "3": "Раковина",
                    "4": "Двойная раковина",
                    "5": "Унитаз",
                    "6": "Биде",
                    "7": "Гигиенический душ",
                }
            for i in range(0, 8):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_45_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_37")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(445):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            converted = {
                    "0": "Ванна",
                    "1": "Душ",
                    "2": "Тропический душ",
                    "3": "Раковина",
                    "4": "Двойная раковина",
                    "5": "Унитаз",
                    "6": "Биде",
                    "7": "Гигиенический душ",
                }
            for i in range(0, 8):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_445_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_37")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(46):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            converted = {
                    "0": "Кабинет",
                    "1": "Мастерская",
                    "2": "Библиотека"
                }

            for i in range(0, 3):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_46_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_45")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(48):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            converted = {
                    "0": "Прачечная",
                    "1": "Кладовая",
                    "2": "Серверная",
                    "3": "Комната для персонала",
                    "4": "Инженерная",
                    "5": "Котельная",
                    "6": "Хозблок"
                }
            updated_status = ",".join(new_status)

            for i in range(0, 7):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_48_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_475")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(52):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)
            
            converted = {
                    "0": "Бар / Кальянная/ Сигарная",
                    "1": "Оружейная",
                    "2": "Сейфовая",
                    "3": "Трофейная/ Музей/ Галерея",
                    "4": "Бассейн/СПА в доме",
                    "5": "Спорт-зона/ Бильярд/ Гейм-зона",
                    "6": "Кинозал",
                    "7": "Приватная комната для взрослых"
                }

            updated_status = ",".join(new_status)

            for i in range(0, 8):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)


            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_52_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_51")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(54):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            converted = {
                    "0": "Терраса у дома",
                    "1": "Крыльцо",
                    "2": "Навес для авто, примыкающий к дому",
                    "3": "Навес для авто отдельностоящий",
                    "4": "Гараж, примыкающий к дому",
                    "5": "Гараж отдельностоящий",
                    "6": "Доп. гараж",
                    "7": "Гостевая парковка",
                }

            for i in range(0, 8):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_54_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_534")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(55):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            converted = {
                    "0": "Беседка — Открытая беседка",
                    "1": "Зона огня",
                    "2": "Релакс-зона",
                    "3": "Баня / СПА",
                    "4": "Детская площадка",
                    "5": "Спортивная площадка",
                    "6": "Гостевой домик"
                }
            for i in range(0, 7):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_55_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_54")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(56):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            converted = {
                    "0": "Геометричность",
                    "1": "Естественность",
                    "2": "Минимализм",
                    "3": "Много зелени",
                    "4": "Функционал важнее стиля",
                }
            for i in range(0, 5):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_56_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_55")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(65):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)

            converted = {
                    "0": "Вода",
                    "1": "Электроэнергия",
                    "2": "Газ",
                    "3": "Канализация",
                    "4": "Высокоскоростной интернет"
                }
            for i in range(0, 5):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_65_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_64")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(70):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)
            converted = {
                    "0": "Снос строений",
                    "1": "Спил и корчевание деревьев",
                    "2": "Пересадка растений",
                    "3": "Уборка мусора",
                    "4": "Земляные работы",
                    "5": "Монтаж подпорных стенок",
                    "6": "Оградить участок"
                }

            for i in range(0, 7):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_70_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_69")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(151):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)
            converted = {
                    "0": "Панорамные окна",
                    "1": "Второй свет",
                    "2": "Плоская кровля с зоной отдыха",
                    "3": "Эркер",
                    "4": "Атриум",
                    "5": "Балкон",
                    "6": "Подвал"
                }

            for i in range(0, 7):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_151_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_14")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(171):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)
            converted = {
                    "0": "Кирпич керамический",
                    "1": "Кирпич ручной формовки",
                    "2": "Ригель ручной формовки",
                    "3": "Декоративная штукатурка",
                    "4": "Натуральное дерево",
                    "5": "Природный камень",
                    "6": "Фасадные панели",
                    "7": "Гибкая керамика"
                }

            for i in range(0, 8):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_171_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_16")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)
        elif handler == str(191):
            markup = InlineKeyboardMarkup(row_width=1)

            
            new_status = status.split(",") if status else []

            if number in new_status:
                new_status.remove(number)
            else:
                new_status.append(number)

            updated_status = ",".join(new_status)
            converted = {
                    "0": "Металлочерепица",
                    "1": "Цементно-песчаная черепица",
                    "2": "Керамика",
                    "3": "Гибкая битумная черепица",
                    "4": "Композитная черепица",
                    "5": "Фальцевая кровля",
                    "6": "Плоская неэксплуатируемая кровля",
                    "7": "Плоская эксплуатируемая кровля",
                }

            for i in range(0, 8):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_191_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_18")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)


        elif handler == str(735):
            for i in range(0, 6):
                data = converted.get(str(i), "Неизвестный вариант")
                text = f"{data}"
                prefix = "✅" if str(i) in new_status else ""
                btn = InlineKeyboardButton(f"{prefix} {text}", callback_data=f"variant_data_{i}_{updated_status}_{handler}")
                markup.add(btn)
            
        
            continueButton = InlineKeyboardButton("Продолжить ▶️", callback_data=("continue_735_"+updated_status))
            # добавляем кнопки назад и продолжить

            backButton = InlineKeyboardButton("◀️ Назад", callback_data="return_72")
            
            markup.add(continueButton, backButton)

            bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=markup)


        

    # Обработчики для цокольного этажа


    if call.data == "basement_yes":
        createdb.exdb("Хорошая идея рассмотрю", 14, call.message.chat.id)
        handler13_1.block4_13_1(call.message, bot)


    if call.data == "nadejnostiidolgovechins":
        createdb.exdb("Надежность и долговечность", 84, call.message.chat.id)
        handler74.block4_40(call.message, bot)
        messages = cache735.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)
    if call.data == "ekomonia":
        createdb.exdb("Экономия бюджета", 84, call.message.chat.id)
        handler74.block4_40(call.message, bot)
        messages = cache735.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)
    if call.data == "wennhosidhtvtyyb":
        createdb.exdb("Ценность времени", 84, call.message.chat.id)
        handler74.block4_40(call.message, bot)
        messages = cache735.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)
    if call.data == "garantayadsfasdfasdf":
        createdb.exdb("Гарантия качества", 84, call.message.chat.id)
        handler74.block4_40(call.message, bot)
        messages = cache735.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)
    if call.data == "viborprofifff":
        createdb.exdb("Выбор профессионалов", 84, call.message.chat.id)
        handler74.block4_40(call.message, bot)
        messages = cache735.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)
    if call.data == "a65465asdfasdf":
        createdb.exdb("Ответственность строителей", 84, call.message.chat.id)
        handler74.block4_40(call.message, bot)
        messages = cache735.get(call.message.chat.id, [])
        for msg in messages:
            bot.delete_message(call.message.chat.id, msg.message_id)

    if call.data == "basement_probably_no":
        createdb.exdb("Скорее нет", 14, call.message.chat.id)
        handler13_1.block4_13_1(call.message, bot)

    if call.data == "dafsdfasfdsafasfadf":
        handler12_1.block4_12_1(call.message, bot)

    if call.data == "basement_info":
        markup = InlineKeyboardMarkup(row_width=1)
        markup.add(InlineKeyboardButton("◀️ Назад", callback_data="dafsdfasfdsafasfadf"))
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(call.message.chat.id, "🔵 <b>Цокольный этаж</b> – это дополнительное пространство с безграничными возможностями: винный погреб, домашний кинотеатр, спортзал или мастерская — подвал решает вопрос нехватки площади. \n\nПо стоимости м2 эта опция всегда выходит дороже, чем создание этажа над землей: дополнительное отопление,  толстые стены.\n\nТакже в нем нередко размещают инженерные системы: отопления, очистки воды.\n\n<i>Правильная гидроизоляция и вентиляция превратят его в комфортную зону, которая увеличит ценность вашего дома.</i>", parse_mode="HTML", reply_markup=markup)


    if call.data == "basement_definitely_no":
        createdb.exdb("Точно нет", 14, call.message.chat.id)
        handler13_1.block4_13_1(call.message, bot)

    if call.data == "bay_window":
        markup = InlineKeyboardMarkup()
        markup.add(backs)
        bot.delete_message(call.message.chat.id, call.message.id)
        bot.send_message(
            call.message.chat.id,
            "🔵 <b>Эркер</b>\n\n"
            "Эркер — это архитектурное «объятие»: выступающая часть дома с окнами создаёт уютный уголок, наполненный светом. Здесь можно устроить зимний сад, каминную зону или место для чтения с панорамным видом. Эркер добавляет дому индивидуальности и делает планировку интереснее.",
            parse_mode="HTML",
            reply_markup=markup
        )

bot.infinity_polling()

