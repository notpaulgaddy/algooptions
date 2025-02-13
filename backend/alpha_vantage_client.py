import os
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries
import requests

load_dotenv()
API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
ts = TimeSeries(key=API_KEY, output_format="json")

def get_stock_price(symbol):
    try:
        data, _ = ts.get_quote_endpoint(symbol=symbol)
        return {
            "symbol": data["01. symbol"],
            "open": data["02. open"],
            "high": data["03. high"],
            "low": data["04. low"],
            "price": data["05. price"],
            "volume": data["06. volume"],
            "latest_trading_day": data["07. latest trading day"],
            "previous_close": data["08. previous close"],
            "change": data["09. change"],
            "percent_change": data["10. change percent"]
        }
    except Exception as e:
        return {"error": str(e)}

# def get_intraday_data(symbol, interval="1min"):
#     url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&outputsize=full&apikey={API_KEY}"
    
#     response = requests.get(url)
    
#     if response.status_code == 200:
#         data = response.json()
#         returnData = {}
        
#         time_series_key = f"Time Series ({interval})"
        
#         if time_series_key in data:
#             start_data = data[time_series_key]
            
#             for each_date, values in start_data.items():
#                 hour = int(each_date[11:13])
#                 minute = int(each_date[14:16])
#                 date_key = each_date[:10]

#                 if 9 <= hour <= 16:
#                     if hour == 9 and minute < 30:
#                         continue

#                     if date_key not in returnData:
#                         returnData[date_key] = []
                    
#                     returnData[date_key].append(values["2. high"])
                
#             return {
#                 "symbol": symbol,
#                 "interval": interval,
#                 "data": returnData
#             }
    
#     return {"error": "Invalid API response or failed to fetch data"}

def get_intraday_data(symbol, interval="1min"):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&outputsize=full&apikey={API_KEY}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("API Response:", data)  # ✅ Debugging Line
        
        time_series_key = f"Time Series ({interval})"
        
        if time_series_key in data:
            return {"message": "API response structure is correct", "data": data[time_series_key]}
        else:
            return {"error": "Invalid API response structure", "response": data}
    
    return {"error": "Failed to fetch data", "status_code": response.status_code}

