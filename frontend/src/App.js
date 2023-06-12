import React, { useEffect, useState } from 'react';
import StockChart from './StockChart';

const App = () => {
  const [stockPrices, setStockPrices] = useState([]);

  useEffect(() => {
    // Fetch stock prices from Flask backend
    fetch('http://localhost:5000/api/stock-prices')  // Update the URL here
      .then((response) => response.json())
      .then((data) => setStockPrices(data.stockPrices))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div>
      <h1>Stock Prices</h1>
      <StockChart stockPrices={stockPrices} />
    </div>
  );
};

export default App;
