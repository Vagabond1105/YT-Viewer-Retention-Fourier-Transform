import yfinance as yf
import numpy as np

def load_price(ticker, period):
    data = yf.download(ticker, period=period, progress=False)

    price = data["Close"].values
    price = price[~np.isnan(price)]

    t = np.arange(len(price))  # time index (days)

    return t, price
