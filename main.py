from src.data.fetcher import get_prices
from src.indicators.indicators import moving_average_trend, rsi
from src.strategy.mia_rsi_strategy import ma_rsi
import config

dat = get_prices(config.TICKERS, period='5d', interval='1h')

for ticker in config.TICKERS:
    trend = moving_average_trend(dat.loc[:, ('Close', ticker)], config.MA_WINDOW)
    rsi_trend = rsi(dat.loc[:, ('Close', ticker)], config.RSI_WINDOW)

    signal = ma_rsi(trend, rsi_trend, config.RSI_THRESHOLD, mode=config.STRATEGY_MODE)

    print(signal)