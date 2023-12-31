import React, { useState, useEffect } from 'react';

const StockList = () => {
  const [stocks, setStocks] = useState([]);
  const [selectedStock, setSelectedStock] = useState(null);

  // Fetch the list of stocks from the backend
  useEffect(() => {
    fetch('http://localhost:5000/api/stocks')
      .then((response) => response.json())
      .then((data) => setStocks(data.stocks))
      .catch((error) => console.error(error));
  }, []);

  // Handle stock click event
  const handleStockClick = (symbol) => {
    setSelectedStock(symbol);
  };

  return (
    <div>
      <h2>Stock List</h2>
      <div style={{ height: '400px', overflow: 'auto' }}>
        {stocks.map((stock) => (
          <div key={stock.symbol} onClick={() => handleStockClick(stock.symbol)}>
            {stock.symbol}
          </div>
        ))}
      </div>
    </div>
  );
};

export default StockList;
