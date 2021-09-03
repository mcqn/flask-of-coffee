# Exceedingly simple flask app for Heroku pipeline tests

from flask import Flask
import random


app = Flask(__name__)

@app.route('/')
def home():
    return '<html><body><h1>Flask of Coffee</h1><p>Hello world</p></body></html>'


if __name__ == '__main__':
    app.run()
