import telebot
from telebot import types


#Технологии

tech1 = types.KeyboardButton('Водородные технологии')
tech2 = types.KeyboardButton('Робототехника')
tech3 = types.KeyboardButton('Машиностроение')
tech4 = types.KeyboardButton('Альтернативная энергетика')
tech5 = types.KeyboardButton('Ботаника')
tech6 = types.KeyboardButton('Исследования')
markup = types.KeyboardButton('Главное меню')
tech = types.ReplyKeyboardMarkup(resize_keyboard = True) .add(tech1, tech2, tech3, tech4, tech5, tech6, markup)# "Это сама менюшка с выравниванием размеров

#Водородные технологии
vt1 = types.KeyboardButton('Водородные генераторы')
vt2 = types.KeyboardButton('Авто на водороде')
vt3 = types.KeyboardButton('Котлы на водороде')
vt4 = types.KeyboardButton('Генераторы на водороде')
vt5 = types.KeyboardButton('Резаки на водороде')
vt6 = types.KeyboardButton('Исследования')
markup = types.KeyboardButton('Главное меню')
vt = types.ReplyKeyboardMarkup(resize_keyboard = True) .add(vt1, vt2, vt3, vt4, vt5, vt6, markup)


#Водородные генераторы
vg1 = types.KeyboardButton('Схемы и инструкции')
vg2 = types.KeyboardButton('Видео')
vg3 = types.KeyboardButton('Проекты')
vg4 = types.KeyboardButton('Исследования')
markup = types.KeyboardButton('Главное меню')
vg = types.ReplyKeyboardMarkup(resize_keyboard = True) .add(vg1, vg2, vg3, vg4, markup)


#Схемы и инструкции

sim = "Очень зорово, что ты решил коснуться этой темы. Здесь ты можешь найти схему, для создания водородного генератора.\nТакже ты можешь добавить свою схему, если есть чем поделиться и тут такого еще нет."
si1 = types.KeyboardButton('Добавить схему')
si2 = types.KeyboardButton('Смотреть схемы')
markup = types.KeyboardButton('Главное меню')
si = types.ReplyKeyboardMarkup(resize_keyboard = True) .add(si1, si2, markup)

#Добавить схему
sas = "Чтобы добавить схему, просто пришли ответное сообщение с файлом схемы. Фаил должен быть подписан и в фомате PDF"

