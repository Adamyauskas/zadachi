from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def indexxx():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def proomm():
    Z = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!', 'Присоединяйся!']
    return f'{Z[0]}<br>{Z[1]}<br>{Z[2]}<br>{Z[3]}<br>{Z[4]}'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081)
