import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip } from 'chart.js';

// Register the required scales and elements
Chart.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip);

const StockChart = ({ stockPrices }) => {
  // Convert the stockPrices data to chart.js format
  const chartData = {
    labels: stockPrices.map((stock) => stock.date),
    datasets: [
      {
        label: 'Stock Price',
        data: stockPrices.map((stock) => stock.bid_price),
        fill: false,
        borderColor: 'rgb(75, 192, 192)',
        tension: 0.1,
      },
    ],
  };

  return (
    <div>
      <h2>Stock Chart</h2>
      <Line data={chartData} />
    </div>
  );
};

export default StockChart;
