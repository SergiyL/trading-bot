import yfinance as yf
import pandas as pd

from src.indicators.indicators import moving_average_trend

def get_prices(tickers, period='1mo'):
    dat = yf.download(tickers, period=period)
    return dat
