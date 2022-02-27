import telebot
from telebot import types

#Программирование
pro1 = types.KeyboardButton('Токены как валюта')
pro2 = types.KeyboardButton('Платформа для взаимодействия')
pro3 = types.KeyboardButton('Предложения')
markup = types.KeyboardButton('Главное меню')
pro = types.ReplyKeyboardMarkup(resize_keyboard = True) .add(pro1, pro2, pro3, markup)# "Это сама менюшка с выравниванием размеров
