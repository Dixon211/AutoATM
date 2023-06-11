
#Algorithms:
#	1. Buy low sell high algorithm

#		-allow window for no trading between first 30min and last 30 minutes of the trading day
#		-needs to set what price the stock was bought at
#		-needs to sell right before hitting this price
#		-needs to sell 10% above what the stock was bought at (rough guess)
#		-3 variables: buy price, stop loss price, profit price = buy price + 10%
#
#       -Sell stocks at EOD

from datetime import datetime

#Stock states
# Unbought
# Bought, hasnt met threshold
# Bought, crossed threshold
class Stock:
    def __init__(self, data):
        self.data = data
        self.state = "UNBOUGHT"
    
    def buy(self):
        self.state = "BOUGHT, NO THRESH"
        pass

    def sell(self):
        self.state = "BOUGHT, THRESH"
        pass

import requests

def getRobinHoodTop100():

    # Set up the API endpoint
    endpoint = "https://api.robinhood.com/marketdata/tops/"

    # Send the API request
    response = requests.get(endpoint, params={"limit": 100})

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the data from the response
        data = response.json()

        # Process the data
        if "results" in data:
            top_stocks = data["results"]
            
            # Print the top 100 stocks
            for stock in top_stocks:
                print(stock["symbol"])
    else:
        print("Error occurred. Status code:", response.status_code)


class BuyLowSellHigh:
    def __init__(self, sellCeilingRatio = 1.1):
        self.sellCeilingRatio = sellCeilingRatio
        self.state = ""

    def run(self):

        # get top 100
        top100 = getRobinHoodTop100()
        print(top100)
        die

        # datetime object containing current date and time
        now = datetime.now()
        
        print("now =", now)

        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("date and time =", dt_string)

#import robin_stocks.robinhood as rh
#import robin_stocks.gemini as gem
#import robin_stocks.tda as tda
import robin_stocks as rs
import os

robin_user = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")
rs.login(username=robin_user,
         password=robin_pass,
         expiresIn=86400,
         by_sms=True)

# Here are some example calls
rs.gemini.gem.get_pubticker("btcusd") # gets ticker information for Bitcoin from Gemini
rs.robinhood.get_all_open_crypto_orders() # gets all cypto orders from Robinhood
rs.tda.get_price_history("tsla") # get price history from TD Ameritrade
rs.logout()
die


if __name__ == "__main__":
    Algo = BuyLowSellHigh()
    Algo.run()