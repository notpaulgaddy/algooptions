from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from alpha_vantage_client import get_stock_price, get_intraday_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/stocks/{symbol}")
async def stock_data(symbol: str):
    """Get latest stock price."""
    return get_stock_price(symbol)

@app.get("/stocks/{symbol}/intraday")
async def stock_intraday(symbol: str, interval: str = "1min"):
    return get_intraday_data(symbol, interval)