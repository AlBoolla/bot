import telebot
from telebot import types

#Коммуникации
kom1 = types.KeyboardButton('Товарообмен')
kom2 = types.KeyboardButton('Услуги')
kom3 = types.KeyboardButton('Криптавалюта')
markup = types.KeyboardButton('Главное меню')

kom = types.ReplyKeyboardMarkup(resize_keyboard = True) .add(kom1, kom2, kom3, markup)# "Это сама менюшка с выравниванием размеров
