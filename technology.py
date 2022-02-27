
import telebot;
from telebot import types


#Технологии
tech1 = types.KeyboardButton('Исследования')
tech2 = types.KeyboardButton('Робототехника')
tech3 = types.KeyboardButton('Водородные технологии')
tech4 = types.KeyboardButton('Альтернативная энергетика')
tech5 = types.KeyboardButton('Ботаника')
tech6 = types.KeyboardButton('Машиностроение')
markup = types.KeyboardButton('Главное меню')
tech = types.ReplyKeyboardMarkup(resize_keyboard = True) .add(tech1, tech2, tech3, tech4, tech5, tech6, markup)# "Это сама менюшка с выравниванием размеров
