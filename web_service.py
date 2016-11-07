#!venv/bin/python
import os

from flask import Flask, jsonify
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
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
