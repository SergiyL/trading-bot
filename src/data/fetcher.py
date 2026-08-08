import yfinance as yf
import pandas as pd

from src.indicators.indicators import moving_average_trend

def get_prices(tickers, period, interval):
    dat = yf.download(tickers, period=period, interval=interval)
    return dat
