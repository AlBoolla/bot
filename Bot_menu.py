import telebot;
from telebot import types
TOKEN = '5168579321:AAEkSPqBEb4UowrMR7col_SFgqhYIuzyavk'

bot = telebot.TeleBot(TOKEN);

@bot.message_handler(commands = ['start']) #Обработчик
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Технологии')
    item2 = types.KeyboardButton('Медицина')
    item3 = types.KeyboardButton('Коммуникации')
    item4 = types.KeyboardButton('Программирование')
    item5 = types.KeyboardButton('Образование')
    item6 = types.KeyboardButton('Дружба народов')

    markup.add(item1, item2, item3, item4, item5, item6 )

    bot.send_message(message.chat.id, "Привет, {0.first_name}!<br>Планета благодарна тебе за то, что ты решил стать гражданином Мира!" .format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == "Технологии":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Исследования')
            item2 = types.KeyboardButton('Робототехника')
            item3 = types.KeyboardButton('Водородные технологии')
            item4 = types.KeyboardButton('Альтернативная энергетика')
            item5 = types.KeyboardButton('Ботаника')
            item6 = types.KeyboardButton('Машиностроение')
            back = types.KeyboardButton('Назад')

            markup.add(item1, item2, item3, item4, item5, item6, back)

            bot.send_message(message.chat.id, "Технологии", reply_markup=markup)

        elif message.text == "Медицина":
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Исследования')
            item2 = types.KeyboardButton('Психология')
            item3 = types.KeyboardButton('Вирусы')
            item4 = types.KeyboardButton('Кости и суставы')
            item5 = types.KeyboardButton('Кожа')
            item6 = types.KeyboardButton('Внутренние органы')
            item7 = types.KeyboardButton('Консультации')
            back = types.KeyboardButton('Назад')

            markup.add(item1, item2, item3, item4, item5, item6, item7, back)

            bot.send_message(message.chat.id, "Медицина".format(message.from_user), reply_markup=markup)

        elif message.text == "Коммуникации":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Связь')
            item2 = types.KeyboardButton('Логистика')
            item3 = types.KeyboardButton('Товарообмен')
            item4 = types.KeyboardButton('Услуги')
            back = types.KeyboardButton('Назад')

            markup.add(item1, item2, item3, item4, back)

            bot.send_message(message.chat.id, "Коммуникации".format(message.from_user), reply_markup=markup)

        elif message.text == "Программирование":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Токены как валюта')
            item2 = types.KeyboardButton('Платформа для взаимодействия')
            item3 = types.KeyboardButton('Новые предложения')
            back = types.KeyboardButton('Назад')

            markup.add(item1, item2, item3, back)

            bot.send_message(message.chat.id, "Программирование".format(message.from_user), reply_markup=markup)



        elif message.text == "Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Технологии')
            item2 = types.KeyboardButton('Медицина')
            item3 = types.KeyboardButton('Коммуникации')
            item4 = types.KeyboardButton('Программирование')
            item5 = types.KeyboardButton('Образование')
            item6 = types.KeyboardButton('Дружба народов')

            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, "Назад", reply_markup=markup)

        elif message.text == "Образование":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Дошкольники')
            item2 = types.KeyboardButton('Дизайн человека')
            item3 = types.KeyboardButton('Физкультура')
            item4 = types.KeyboardButton('Математика')
            item5 = types.KeyboardButton('Речь и написание')
            item6 = types.KeyboardButton('Химия')
            item7 = types.KeyboardButton('Физика')
            item8 = types.KeyboardButton('Астрономия')
            item9 = types.KeyboardButton('Новые способности')
            back = types.KeyboardButton('Назад')

            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, back)

            bot.send_message(message.chat.id, "Образование".format(message.from_user), reply_markup=markup)

        elif message.text == "Дружба народов":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Коммуникация между странами')
            item2 = types.KeyboardButton('Логистика')
            item3 = types.KeyboardButton('Вопросы к обсуждению')
            back = types.KeyboardButton('Назад')

            markup.add(item1, item2, item3, back)

            bot.send_message(message.chat.id, "Дружба народов".format(message.from_user), reply_markup=markup)



bot.polling(none_stop = True)