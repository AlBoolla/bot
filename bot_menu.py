import telebot
from telebot import types
import mainmenu, technology, kommunications, medicine, programming, education, frendpipels


TOKEN = '5168579321:AAEkSPqBEb4UowrMR7col_SFgqhYIuzyavk'

bot = telebot.TeleBot(TOKEN);

@bot.message_handler(commands = ['start']) #Обработчик
def start(message):
    bot.send_message(message.chat.id, "Привет, {0.first_name}!".format(message.from_user), reply_markup=mainmenu.markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == "Главное меню":
            bot.send_message(message.chat.id, "Главное меню", reply_markup=mainmenu.markup)
        elif message.text == "Технологии":
            bot.send_message(message.chat.id, "Технологии", reply_markup=technology.tech)
        elif message.text == "Медицина":
            bot.send_message(message.chat.id, "Медицина", reply_markup=medicine.med)
        elif message.text == "Коммуникации":
            bot.send_message(message.chat.id, "Коммуникации", reply_markup=kommunications.kom)
        elif message.text == "Программирование":
            bot.send_message(message.chat.id, "Программирование", reply_markup=programming.pro)
        elif message.text == "Образование":
            bot.send_message(message.chat.id, "Образование", reply_markup=education.ed)
        elif message.text == "Дружба народов":
            bot.send_message(message.chat.id, "Дружба народов", reply_markup=frendpipels.fr)
        else:
            bot.send_message(message.chat.id, "Друг, я верю что ты разберешься без меня", reply_markup=mainmenu.markup)





bot.polling(none_stop = True)
