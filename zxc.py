import telebot 
from dotenv import dotenv_values
import sqlite3
config = dotenv_values(".env")


bot = telebot.TeleBot(config['TELEGRAM_TOKEN'])
print('bot is running')

@bot.message_handler(commands=['start','help'])
def amogus2(message):
    conn = sqlite3.connect('superheroes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT count(*) FROM superhero')
    data = cursor.fetchall()
    conn.close()

    bot.send_message(message.chat.id, f'i have info of {data[0][0]} superhero')

@bot.message_handler(commands=['good'])
def amogus3(message):
    conn = sqlite3.connect('superheroes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT count(*) FROM superhero WHERE alignment_id = 1')
    data = cursor.fetchall()
    conn.close()

    bot.send_message(message.chat.id, f'i have info of good{data[0][0]} superhero')


@bot.message_handler(commands=['evil'])
def amogus4(message):
    conn = sqlite3.connect('superheroes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT count(*) FROM superhero WHERE alignment_id = 2')
    data = cursor.fetchall()
    conn.close()

    bot.send_message(message.chat.id, f'i have info of evil {data[0][0]} superhero')

@bot.message_handler(commands=['find'])
def amogus4(message):
    conn = sqlite3.connect('superheroes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT count(*) FROM superhero WHERE alignment_id = 2')
    data = cursor.fetchall()
    conn.close()

    bot.send_message(message.chat.id, f'i have info of evil {data[0][0]} superhero')


# @bot.message_handler(content_types=['cat'])
# def amogus3(message):
#     with open('asd.png', 'rb') as file:
#         bot.send_photo(message.chat.id, file)

@bot.message_handler(content_types=['text'])
def amogus(message):
    print(f'User {message.from_user.first_name} id={message.chat.id}: {message.text}')
    bot.send_message(message.caht.id, 'Hw' + message.text)



bot.polling(none_stop=True)

