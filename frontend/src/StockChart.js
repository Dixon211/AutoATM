import React from 'react';
import { Line } from 'react-chartjs-2';

const StockChart = ({ stockPrices }) => {
  // Extracting labels and data from stockPrices
  const labels = stockPrices.map((price) => price.date);
  const data = stockPrices.map((price) => price.price);

  // Chart configuration
  const chartData = {
    labels: labels,
    datasets: [
      {
        label: 'Stock Prices',
        data: data,
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
      },
    ],
  };

  return (
    <div>
      <Line data={chartData} />
    </div>
  );
};

export default StockChart;
