#!venv/bin/python
from flask import Flask, jsonify, json
import requests
import fiso_scraper

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello World"

@app.route('/price-changes', methods=['GET'])
def get_tasks():
    price_changes = fiso_scraper.get_price_changes()
    return jsonify(price_changes)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
