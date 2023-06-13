import React from 'react';
import { Line } from 'react-chartjs-2';
import { Chart, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip } from 'chart.js';

// Register the required scales and elements
Chart.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip);

const StockChart = ({ stockPrices }) => {

    if (!stockPrices) {
        return null; // or any other fallback component or loading indicator
    }

    // Get the symbol from the first price in stockPrices
    const symbol = stockPrices.length > 0 ? stockPrices[0].symbol : '';

    // Convert the stockPrices data to chart.js format
    const chartData = {

        labels: stockPrices.map((stock) => stock.time),
        datasets: [
            {
                label: 'Stock Price',
                data: stockPrices.map((stock) => stock.Close),
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1,
            },
        ],
    };

    return (
        <div>
            <h2>{symbol}</h2>
            <Line data={chartData} />
        </div>
    );
};

export default StockChart;
