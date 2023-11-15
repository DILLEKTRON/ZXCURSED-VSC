

from flask import Flask, Response , request
from flask_cors import CORS
from uuid import uuid4
import json

def delete_user(name):
    users.remove(name)
name = []
tokens = {}
msg = ''

app = Flask(__name__)
CORS(app)

def generate_token():
    token = str(uuid4())
    return token



# /method?argumen1=value1&argumen2=value2
# http://127.0.0.1:5000

users = {
    'name': '',
    'token': ''
}

@app.route("/")
def main():
    return "commands: /auth, /logout, /send, /getall"

# x = 'name'
@app.route("/auth")
def auth(): 
    x = request.args.get('name')
    token = generate_token()
    print(f"Сгенерированный токен: {token}")
    if x == None:
        return "Ошибка авторизации"
    if x in users:
        return "Такой пользователь уже авторизован"
    else:
        print (x,token)
        users['name'] = users
        tokens['token'] = token
        return x, token

@app.route("/logout")
def logout():
    for key,value in users.items():
        if value == users['name']:
            del users[key]
    return "Вы  успешно вышли"

@app.route("/send")
def send():
    x = request.args.get('name')
    c = request.args.get('message')
    x = users.get('name')
    if c == None:
        return "Ошибка отправки сообщения"
    if x == None:
        return "Пользователь сдох нахуй выблядок ебанный сын ебанной бляди отсталый сын бляди"
    if tokens == None:
        return "Ошибка токена"
    else:
        print(x,c,tokens['token'])
        return x,c,tokens['token']

@app.route("/getall")
def getall():
    if request.args.get('token') not in users.values():
        return Response("Иди нахуй")
    # for key,value in users.items():
    #     if value == tokens['token']:
    #         return Response(json.dumps(msg))


if __name__ == "__main__":
    print('RABOTAEM')
    app.run(debug=True)




























