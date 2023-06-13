from flask import Flask, jsonify, request
from flask_cors import CORS
import algos
from dotenv import load_dotenv
from datetime import datetime
import robin_stocks.robinhood as r
import yfinance as yf
import os
import requests
import json
import pandas as pd

load_dotenv()

here = os.path.dirname(os.path.abspath(__file__))

robin_user = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")
r.login(username=robin_user, password=robin_pass, expiresIn=86400, by_sms=True)

app = Flask(__name__)
CORS(app)
from datetime import datetime
import time


def getTop100():

    # 1 year ago
    now = datetime.now()

    outfilename = os.path.join(
        here, "histories", now.strftime("%m%d%Y") + "_top100.json"
    )

    if os.path.exists(outfilename):
        # load file if available
        # # Read JSON file into a DataFrame
        with open(outfilename, "r") as f:
            top100 = json.loads(f.read())

    else:
        top100 = r.get_top_100()
        # write for future reference
        with open(outfilename, "w+") as f:
            f.write(json.dumps(top100))

    return top100


def getHistory(symbol):
    start_time = datetime(2022, 6, 11)  # Set your desired start time
    os.makedirs(os.path.join(here, "histories"), exist_ok=True)
    outfilename = os.path.join(
        here, "histories", start_time.strftime("%m%d%Y") + "_" + symbol + ".json"
    )
    1
    if os.path.exists(outfilename):
        # load file if available
        # # Read JSON file into a DataFrame
        stock_prices = pd.read_json(outfilename, orient="index")

    else:
        stock = yf.Ticker(symbol)
        stock_prices = stock.history(start=start_time, period="1y", interval="1h")

        # write for future reference
        stock_prices.to_json(outfilename, orient="index")

    # Resample to 1-hour intervals and interpolate missing values
    stock_prices_resampled = stock_prices.asfreq("30min", method="ffill")

    new_additions = stock_prices_resampled[~stock_prices_resampled.index.isin(stock_prices.index)]
    stock_prices_resampled.loc[new_additions.index, 'Volume'] = 0


    # stock_prices_resampled_na = stock_prices.asfreq('30min', method='fillna')
    # stock_prices_resampled["Volume"] = stock_prices_resampled_na["Volume"]

    stock_prices_resampled["time"] = stock_prices_resampled.index.strftime(
        "%Y-%m-%d %H:%M"
    )
    stock_prices_resampled["symbol"] = symbol

    return stock_prices_resampled[-2000:]


# Endpoint to fetch a list of 100 stocks
@app.route("/api/stocks", methods=["GET"])
def get_stocks():
    # get top 100 stocks
    stocks = r.get_top_100()
    return jsonify({"stocks": stocks})


# Endpoint to fetch historical data for a stock
@app.route("/api/stock-history", methods=["GET"])
def get_stock_history():
    symbol = request.args.get("symbol")

    if not symbol:
        return jsonify({"error": "Symbol parameter is required."}), 400

    print("Getting stock history for " + symbol)

    try:
        stock_prices = getHistory(symbol=symbol)
        retval = '{"stockPrices": ' + stock_prices.to_json(orient="records") + "}"
        return retval
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Define your Flask routes and logic here
@app.route("/api/stock-prices", methods=["GET"])
def get_stock_prices():
    print("received req")

    # get top stocks
    top100listOfDicts = getTop100()
    symbol = top100listOfDicts[0]["symbol"]

    # Fetch 2 years of 5-minute interval historical data for symbol
    # stock_prices = r.stocks.get_stock_historicals(symbol, interval='5minute', span='year')
    # stock_prices = r.stocks.get_stock_historicals(symbol, interval='day', span='5year')
    stock_prices = getHistory(symbol=symbol)
    print(stock_prices.columns)

    retval = '{"stockPrices": ' + stock_prices.to_json(orient="records") + "}"

    return retval


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)


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
            config = {
                key: value
                for key, value in self.options.items()
                if key in self.cfg.settings and value is not None
            }
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
