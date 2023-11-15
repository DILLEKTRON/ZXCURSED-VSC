
from flask import Flask, Response , request
from flask_cors import CORS
from uuid import uuid4
import json
import time 
import datetime
timestamp = time.time()



def delete_user(name):
    users.remove(name)


app = Flask(__name__)
CORS(app)

def generate_token():
    token = str(uuid4())
    return token



# /method?argumen1=value1&argumen2=value2
# http://127.0.0.1:5000


tokens = {}

messages = []

msg = {}

users = {}


@app.route("/")
def main():
    return "commands: /auth, /logout, /send, /getall"

@app.route("/auth")
def auth(): 
    username = request.args.get('name')
    if username is None:
        return "Ошибка авторизации"
    if username in users:
        return "Такой пользователь уже авторизован"
    else:
        token = generate_token()
        print(f"Сгенерированный токен: {token}")
        print (username,token)
        users[username] = token
        tokens[username] = token
        return f"{username}, {token}"

@app.route("/logout")
def logout():
    username_to_logout = request.args.get('name')
    if username_to_logout is None:
        return "Ошибка выхода"
    if username_to_logout in users:
        del users[username_to_logout]
        return f"Пользователь {username_to_logout} успешно вышел"
    else:
        return f"Пользователь {username_to_logout} не найден"

@app.route("/send")
def send():
    username = request.args.get('name')
    message = request.args.get('message')
    if message is None:
        return "Ошибка отправки сообщения"
    if username not in users:
        return "Пользователь не найден"
    if username not in tokens:
        return "Ошибка токена"
    else:
        timestamp = datetime.datetime.now().isoformat()
        msg_data = {"username": username, "message": message, "timestamp": timestamp}
        messages.append(msg_data)
        print(username, message)
        return f"{username}, {message}"

# Это если надо токены выводить
# tokens[username]
# {tokens[username]}

@app.route("/getall")
def getall():
    username = request.args.get('name')
    if username not in users:
        return Response("Вы не можете получить доступ к чату",content_type='text/plain; charset=utf-8')

    user_messages = [{"username": msg["username"], "message": msg["message"], "timestamp": msg["timestamp"]} for msg in messages]
    response_data = json.dumps(user_messages, ensure_ascii=False)
    return Response(response_data, content_type='application/json; charset=utf-8')

if __name__ == "__main__":
    print('RABOTAEM')
    app.run(debug=True)


# for key,value in users.items():
#     if value == users['name']:
#         del users[key]
# return "Вы  успешно вышли"



























    #     if value == tokens['token']:
    #         return Response(json.dumps(msg))


if __name__ == "__main__":
    print('RABOTAEM')
    app.run(debug=True)




























