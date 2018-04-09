from flask import Flask
from flask import request, render_template

import serial_python as serial

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def hello():
    num = serial.get_distance()
    if(num == 'null'):
        num = 1
    return str(num)

@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run("localhost", 8080)