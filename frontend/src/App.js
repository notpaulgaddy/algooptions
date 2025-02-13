import React, { useState } from "react";
import { getStockData } from "./api/data";

const StockInfo = () => {
  const [symbol, setSymbol] = useState("");
  const [data, setData] = useState(null);

  const fetchStock = async () => {
    const stockData = await getStockData(symbol);
    setData(stockData);
  };

  return (
    <div>
      <input
        type="text"
        placeholder="Enter stock symbol"
        value={symbol}
        onChange={(e) => setSymbol(e.target.value.toUpperCase())}
      />
      <button onClick={fetchStock}>Get Stock Price</button>

      {data && (
        <div>
          <h3>{data.symbol} Price: ${data.price}</h3>
          <p>Change: {data.change} ({data.percent_change})</p>
          <h3>Last Trading Day's Open: {data.open}</h3>
          <h3>Last Trading Day's Close: {data.previous_close}</h3>
          <h3>Last Trading Day's High: {data.high}</h3>
          <h3>Last Trading Day's Low: {data.low}</h3>
        </div>
      )}
    </div>
  );
};

export default StockInfo;