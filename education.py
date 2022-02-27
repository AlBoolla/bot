import telebot
from telebot import types

#Образование
ed1 = types.KeyboardButton('Дошкольники')
ed2 = types.KeyboardButton('Школьники')
ed3 = types.KeyboardButton('Профессиональное')
ed4 = types.KeyboardButton('Техническое')
ed5 = types.KeyboardButton('Высшее')
ed6 = types.KeyboardButton('Курсы')
ed7 = types.KeyboardButton('Дизайн человека')
markup = types.KeyboardButton('Главное меню')
ed = types.ReplyKeyboardMarkup(resize_keyboard = True) .add(ed1, ed2, ed3, ed4, ed5, ed6, ed7, markup)# "Это сама менюшка с выравниванием размеров

