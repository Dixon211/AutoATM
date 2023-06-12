from flask import Flask, jsonify
from flask_cors import CORS
import algos
from dotenv import load_dotenv
from datetime import datetime
import robin_stocks.robinhood as r
import os
import requests
load_dotenv()

robin_user = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")
r.login(username=robin_user,
        password=robin_pass,
        expiresIn=86400,
        by_sms=True)

app = Flask(__name__)
CORS(app)


# Define your Flask routes and logic here
@app.route('/api/stock-prices')
def get_stock_prices():
    print("received req")

    # get top stocks
    top100listOfDicts = r.get_top_100()
    symbol = top100listOfDicts[0]["symbol"]

    # Fetch 2 years of 5-minute interval historical data for symbol
    #stock_prices = r.stocks.get_stock_historicals(symbol, interval='5minute', span='year')
    stock_prices = r.stocks.get_stock_historicals(symbol, interval='hour', span='month')

    print(stock_prices[0].keys())
    
    return jsonify({'stockPrices': stock_prices})

def runAsUnicorn():

    # Run the Flask app with Unicorn server
    from multiprocessing import cpu_count
    from gunicorn.app.base import BaseApplication

    class FlaskApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super().__init__()

        def load_config(self):
            config = {key: value for key, value in self.options.items() if key in self.cfg.settings and value is not None}
            for key, value in config.items():
                self.cfg.set(key.lower(), value)

        def load(self):
            return self.application

    options = {
        "bind": "0.0.0.0:5000",  # Replace with your desired host and port
        "workers": cpu_count() * 2 + 1,
        "accesslog": "-",  # Print access logs to stdout
    }

    FlaskApplication(app, options).run()

if __name__ == "__main__":
    app.run(debug=True)
