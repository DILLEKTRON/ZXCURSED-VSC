
import telebot
from telebot import types
import sqlite3
from dotenv import dotenv_values

config = dotenv_values(".env")
bot = telebot.TeleBot(config['TELEGRAM_TOKEN'])
print('Pivo lietsa')

@bot.message_handler(commands=['start',  'Привет'])
def zxc_start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} я ПивоШоп, только тут самое лучшее Телеграмм пиво')

@bot.message_handler(commands=['help'])
def zxc_help(message):
    bot.send_message(message.chat.id, 'Команды для старта: start, Привет')

@bot.message_handler(content_types=['text'])
def zxc_text(message):
    conn = sqlite3.connect('Pivo.db')
    cursor = conn.cursor()

    if message.text.lower() == 'beer':
        cursor.execute('SELECT category_name FROM categories')
        categories = cursor.fetchall()

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        for category in categories:
            markup.add(types.KeyboardButton(category[0]))

        bot.send_message(message.chat.id, "Выберите марку пива:", reply_markup=markup)
    else:
        category_name = message.text.lower()

        cursor.execute('SELECT Pivo, Price, Image FROM item WHERE Pivo LIKE ?', ('%' + category_name + '%',))
        result = cursor.fetchall()
        cursor.close()

        if result:
            for row in result:
                response_text = f"{row[0]} - {row[1]} руб."
                response_image = row[2] 

                bot.send_photo(message.chat.id, open(response_image, 'rb'), caption=response_text)
        else:
            bot.send_message(message.chat.id, 'Извините, я не понимаю что это, это марка пива?')

bot.polling(none_stop=True)
