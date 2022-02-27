import telebot
from telebot import types


#Медицина
med1 = types.KeyboardButton('Исследования')
med2 = types.KeyboardButton('Психология')
med3 = types.KeyboardButton('Вирусы')
med4 = types.KeyboardButton('Кости и суставы')
med5 = types.KeyboardButton('Кожа')
med6 = types.KeyboardButton('Внутренние органы')
med7 = types.KeyboardButton('Консультации')
markup = types.KeyboardButton('Главное меню')
med = types.ReplyKeyboardMarkup(resize_keyboard = True) .add(med1, med2, med3, med4, med5, med6, med7, markup)# "Это сама менюшка с выравниванием размеров
