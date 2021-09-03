# Exceedingly simple backend mockup to allow for Armie testing

from flask import Flask, send_from_directory, jsonify
import random


app = Flask(__name__)

@app.route('/')
def home():
    return '<html><body><h1>Flask of Coffee</h1><p>Hello world</p></body></html>'


if __name__ == '__main__':
    app.run()
