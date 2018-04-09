from flask import Flask
from flask import request, render_template

import serial_python as serial

app = Flask(__name__)


@app.route("/")
def hello():
    num = serial.get_distance()
    if(num == 'null'):
        num = 1
    return str(num)

@app.route('/sketch.js')
def sketch():
    return render_template('sketch.js')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/p5.min.js')
def p5():
    return render_template('p5.min.js')    

if __name__ == '__main__':
    app.run("localhost", 8080)