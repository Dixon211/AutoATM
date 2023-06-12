from flask import Flask, jsonify

app = Flask(__name__)

# Define your Flask routes and logic here
@app.route('/api/stock-prices')
def get_stock_prices():
    print("received req")

    # Retrieve stock prices from your data source
    stock_prices = [
        {'date': '2023-06-10', 'price': 100},
        {'date': '2023-06-11', 'price': 105},
        {'date': '2023-06-12', 'price': 95},
        # ... more data
    ]
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
