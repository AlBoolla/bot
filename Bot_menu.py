import telebot;
bot = telebot.TeleBot('5225194571:AAHwL6mPR28W2R06EkEV15sxn-F2vkH3Mfo');

@bot.message_handler(content_types=['text']) #объявляем метод для получения текстовых сообщений
def get_text_messages(message):

@bot.message_handler(content_types=['text', 'document', 'audio']) #объявили слушателя для текстовых сообщений и метод их обработки. Поле content_types может принимать разные значения, и не только одно, например

if message.text == "Привет":
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши привет")
else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)