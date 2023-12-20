
import telebot
from telebot import types
import sqlite3
from dotenv import dotenv_values
import time 
import datetime
timestamp = time.time()


config = dotenv_values(".env")
bot = telebot.TeleBot(config['TELEGRAM_TOKEN'])
print('Pivo lietsa')

conn = sqlite3.connect('Pivo.db')
cursor = conn.cursor()



def get_balance(Player):
    conn = sqlite3.connect('Pivo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT Balance FROM Users WHERE id = ?', (Player,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else 0

def update_balance(Player, amount):
    with sqlite3.connect('Pivo.db') as conn:
        cursor = conn.cursor()
        cursor.execute('UPDATE Users SET Balance = Balance - ? WHERE id = ?', (amount, Player))
        conn.commit()


def add_purchase_to_history(user_id, first_name, beer_name, beer_price):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
    INSERT INTO PurchaseHistory (user_id, first_name, beer_name, price, purchase_time)
    VALUES (?, ?, ?, ?, ?)
    ''', (user_id, first_name, beer_name, beer_price, current_time))
    conn.commit()


@bot.message_handler(commands=['start', 'Привет'])
def zxc_start(message):
    Player = message.from_user.id
    conn = sqlite3.connect('Pivo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Users WHERE id=?", (Player,))
    user_tyt = cursor.fetchone()

    if not user_tyt:
        cursor.execute("INSERT INTO Users (id, Balance) VALUES (?, 0)", (Player,))
        cursor.execute("INSERT INTO PurchaseHistory (user_id) VALUES (?)", (Player,))
        conn.commit()
        print(f"Added new user with id: {Player}") 
    else:
        print(f"Returning user with id: {Player}")  

    cursor.close()
    conn.close()

    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} я ПивоШоп!')
    bot.send_photo(message.chat.id, open('pudge.jpg', 'rb'))
    bot.send_message(message.chat.id, "Меню:", reply_markup=main_menu(Player))


def main_menu(Player):
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Давай давай, нажми сюда", callback_data="deposit"))
    markup.add(types.InlineKeyboardButton("Ну и сколько у тебя денег?", callback_data="check_balance"))
    markup.add(types.InlineKeyboardButton("Наш восхительный выбор светлого", callback_data="beer_categories"))
    markup.add(types.InlineKeyboardButton("Сколько уже набрал литров?", callback_data="view_history"))
    markup.add(types.InlineKeyboardButton(text="Мой пивной кумир", url='https://www.youtube.com/channel/UCByOkBSMkZaUOB2xI0R9Hlg'))
    return markup

@bot.callback_query_handler(func=lambda call: call.data == "deposit")
def callback_deposit(call):
    bot.send_message(call.message.chat.id, "Сколько хотите нам отдать?😍")
    bot.register_next_step_handler(call.message, handle_deposit)




def handle_deposit(message):
    try:
        amount = int(message.text)
        if amount <= 0:
            bot.send_message(message.chat.id,'Ты че вообще дурак, себя ограбь')
        else:
            Player = message.from_user.id
            conn = sqlite3.connect('Pivo.db')
            cursor = conn.cursor()
            cursor.execute('UPDATE Users SET Balance = Balance + ? WHERE id = ?', (amount, Player))
            conn.commit()
            cursor.close()  
            conn.close()
            bot.send_message(message.chat.id, f'Деньги пришли, пока 👋 {amount} руб.', reply_markup=main_menu(Player))
    except ValueError:
        bot.send_message(message.chat.id, 'Что ты творишь?')




@bot.callback_query_handler(func=lambda call: call.data == "check_balance")
def callback_check_balance(call):
    user_id = call.from_user.id
    balance = get_balance(user_id)
    bot.send_message(call.message.chat.id, f"Ваш текущий баланс: {balance} руб.", reply_markup=main_menu(user_id))


@bot.callback_query_handler(func=lambda call: call.data == "beer_categories")
def callback_show_beer_categories(call):
    conn = sqlite3.connect('Pivo.db')
    cursor = conn.cursor()
    

    cursor.execute('SELECT category_name FROM categories')
    categories = cursor.fetchall()

    markup = types.InlineKeyboardMarkup()
    for category in categories:
        markup.add(types.InlineKeyboardButton(category[0], callback_data=f"category_{category[0]}"))

    bot.send_message(call.message.chat.id, "Выберите марку пива:", reply_markup=markup)

    cursor.close()
    conn.close()

@bot.callback_query_handler(func=lambda call: call.data.startswith("buy_"))
def callback_buy(call):
    category_name = call.data.split("_", 1)[1]
    conn = sqlite3.connect('Pivo.db')
    cursor = conn.cursor()

    cursor.execute('SELECT Pivo, Price FROM item WHERE Pivo = ?', (category_name,))
    result = cursor.fetchone()

    if result:
        beer_name, beer_price = result
        update_balance(call.from_user.id, amount=beer_price)


    # if result:
    #     cursor = conn.cursor()
    #     update_balance(call.from_user.id, result[0])
    #     beer_name, beer_price = result
    #     Player = call.from_user.id
    #     user_balance = get_balance(Player)
    #     conn.commit()
        
        bot.answer_callback_query(call.id, f"Ураааа пивасик {beer_name} за {beer_price} руб!")
    else:
        bot.answer_callback_query(call.id, "Пива не будет😥😥.")

# def update_balance(Player, amount):
#     conn = sqlite3.connect('Pivo.db')
#     cursor.execute('UPDATE Users SET Balance = Balance - ? WHERE id = ?', (amount, Player))
#     conn.commit()
#     cursor.close()
#     conn.close()




    

@bot.callback_query_handler(func=lambda call: call.data.startswith("category_"))
def callback_show_beer_by_category(call):
    category_name = call.data.split("_", 1)[1]
    conn = sqlite3.connect('Pivo.db')
    cursor = conn.cursor()

    cursor.execute('SELECT Pivo, Price, Image FROM item WHERE Pivo LIKE ?', (category_name,))
    result = cursor.fetchall()

    if result:
        for row in result:
            response_text = "\n".join([f"{row[0]} - {row[1]} руб." for row in result if len(row) >= 2])
            response_image = row[2] 
            buy_button = types.InlineKeyboardButton("Купить", callback_data=f"buy_{category_name}")
            markup = types.InlineKeyboardMarkup().add(buy_button)
            bot.send_message(call.message.chat.id, response_text)
            bot.send_photo(call.message.chat.id, open(response_image, 'rb'), caption=response_text,reply_markup=markup)
        # if get_balance(Player) < beer_price:
    
    # if result:
    #     beer_name, beer_price, beer_image = result[0]
    #     Player = call.from_user.id
    #     user_first_name = call.from_user.first_name

    #     if get_balance(Player) < beer_price:
    #         bot.send_message(call.message.chat.id, "У вас недостаточно средств для покупки этого пива.")
    #         return
    else:
        bot.send_message(call.message.chat.id, "У вас недостаточно средств для покупки этого пива.")
        return
    

@bot.callback_query_handler(func=lambda call: call.data == "view_history")
def callback_view_history(call):
    user_id = call.from_user.id
    conn = sqlite3.connect('Pivo.db')
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT beer_name, price, purchase_time FROM PurchaseHistory WHERE user_id = ? ORDER BY purchase_time DESC', (user_id,))
        purchases = cursor.fetchall()

        print(f"User ID: {user_id}, Purchases: {purchases}")  # Логирование

        if purchases:
            response_text = "Ваша история покупок:\n\n"
            for purchase in purchases:
                beer_name, price, purchase_time = purchase
                response_text += f"{beer_name} - {price} руб. ({purchase_time})\n"
            
            bot.send_message(call.message.chat.id, response_text)
        else:
            print(f"No purchases found for user ID: {user_id}")  # Дополнительное логирование
            bot.send_message(call.message.chat.id, "У тебя нету пива((")

    except Exception as e:
        print(f"Error fetching purchase history for user {user_id}: {e}")

    finally:
        cursor.close()
        conn.close()

        

        


bot.polling(none_stop=True)
