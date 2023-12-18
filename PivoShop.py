
import telebot
from telebot import types
import sqlite3
from dotenv import dotenv_values

config = dotenv_values(".env")
bot = telebot.TeleBot(config['TELEGRAM_TOKEN'])
print('Pivo lietsa')

@bot.message_handler(commands=['start', 'pivo', 'Привет'])
def zxc_start(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} я ПивоШоп, только тут самое лучшее Телеграмм пиво')

@bot.message_handler(commands=['help'])
def zxc_help(message):
    bot.send_message(message.chat.id, 'Команды для старта: start, pivo, Привет')

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

        bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup)
    else:
        category_name = message.text.lower()
        some_other_value = 'some value' 

        cursor.execute('SELECT item.Pivo, item.Price FROM item JOIN categories ON item.category_id = categories.id WHERE categories.category_name = ? AND some_other_column = ?', (category_name, some_other_value))
        result = cursor.fetchall()
        cursor.close()

        if result:
            response = "\n".join([f"{row[0]} - {row[1]} руб." for row in result])
            bot.send_message(message.chat.id, response)
        else:
            bot.send_message(message.chat.id, 'Извините, я не могу найти информацию для вашего запроса.')

bot.polling(none_stop=True)
