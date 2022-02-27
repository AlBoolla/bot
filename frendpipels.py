import telebot
from telebot import types

#Дружба народов
fr1 = types.KeyboardButton('Коммуникация между странами')
fr2 = types.KeyboardButton('Логистика')
fr3 = types.KeyboardButton('Совместные проекты')
markup = types.KeyboardButton('Главное меню')
fr = types.ReplyKeyboardMarkup(resize_keyboard = True) .add(fr1, fr2, fr3, markup)# "Это сама менюшка с выравниванием размеров
