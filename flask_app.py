
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from datetime import date
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello!! :), from Bm'
@app.route('/today')
def hello_world():
    return date.today()

