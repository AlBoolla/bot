import telebot;
from telebot import types


item1 = types.KeyboardButton('Технологии')
item2 = types.KeyboardButton('Медицина')
item3 = types.KeyboardButton('Коммуникации')
item4 = types.KeyboardButton('Программирование')
item5 = types.KeyboardButton('Образование')

markup =types.ReplyKeyboardMarkup(resize_keyboard = True).add(item1, item2, item3, item4, item5)

