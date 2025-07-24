from flask import Flask, render_template, request, jsonify
from threading import Condition
import threading
from commands import *
from teste import *

def handleCommand(data):
    if(data == TEST_STEPPERS):
        test()

app = Flask(__name__)

@app.route('/post', methods =['POST'])
def get_data():
    data = request.get_data()
    handleCommand(data)
    return "OK", 200

@app.route('/')
def index():
    return render_template('index.html')

if( __name__ == "__main__"):
    app.run(host="192.168.2.68", port="8000", threaded = True)
