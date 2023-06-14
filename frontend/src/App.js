import React, { useEffect, useState } from 'react';
import StockChart from './StockChart';

const App = () => {
  const [stockPrices, setStockPrices] = useState([]);
  const [stockList, setStockList] = useState([]);

  useEffect(() => {
    // Fetch stock prices from Flask backend
    fetch('http://localhost:5000/api/stock-prices')
      .then((response) => response.json())
      .then((data) => setStockPrices(data.stockPrices))
      .catch((error) => console.error(error));

    // Fetch stock list from Flask backend
    fetch('http://localhost:5000/api/stocks')
      .then((response) => response.json())
      .then((data) => setStockList(data.stocks))
      .catch((error) => console.error(error));
  }, []);

  const handleStockClick = (symbol) => {
    console.log("handling click")
    // Fetch historical data for the selected stock
    fetch(`http://localhost:5000/api/stock-history?symbol=${symbol}`)
      .then((response) => response.json())
      .then((data) => setStockPrices(data.stockPrices))
      .catch((error) => console.error(error));
  };

  return (
    <div>
      <h1>Stock Prices</h1>
      <div>
        {stockList.map((stock) => (
          <button key={stock.symbol} onClick={() => handleStockClick(stock.symbol)}>
            {stock.symbol}
          </button>
        ))}
      </div>
      <StockChart stockPrices={stockPrices} />
    </div>
  );
};

export default App;
