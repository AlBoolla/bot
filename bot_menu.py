import telebot
import json
from telebot import types
import mainmenu, technology, kommunications, medicine, programming, education


TOKEN = '5168579321:AAEkSPqBEb4UowrMR7col_SFgqhYIuzyavk'
URL = 'https://api.telegram.org/bot'

bot = telebot.TeleBot(TOKEN);

@bot.message_handler(commands = ['start']) #Обработчик
def start(message):
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Тут ты можешь присоедениться к проекту который кто-то уже разрабатывает или создать свой в любой сфере".format(message.from_user), reply_markup=mainmenu.markup)

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
        else:
            bot.send_message(message.chat.id, "Я верю, что ты разберешься.", reply_markup=mainmenu.markup)


@bot.message_handler(content_types=['file'])
def bot_message_file(message):
    if message.chat.type == 'private':
        if message.file == 'True':
            print("Test print")







bot.polling(none_stop = True)
