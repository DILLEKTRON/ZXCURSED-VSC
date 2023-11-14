
from flask import Flask, Response , request
from flask_cors import CORS
from uuid import uuid4



def delete_user(name):
    users.remove(name)
name = ''
tokens = {}

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

x = 'name'
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
        users['name'] = x
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
    if c == None:
        return "Ошибка отправки сообщения"
    else:
        print(c,x,tokens['token'])
        return c,x,tokens['token']

@app.route("/getall")
def getall():
    m = [
        {'name': 'Max', 'message': '', 'timestamp':123},
    ]
    return "Hello, World!"


if __name__ == "__main__":
    print('RABOTAEM')
    app.run(debug=True)























