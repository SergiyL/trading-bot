from src.data.fetcher import get_prices
from src.indicators.indicators import moving_average_trend, rsi
from src.strategy.simple_strategy import check_buy_signal

tickers = ['GOOGL', 'META', 'NFLX']
dat = get_prices(tickers, '1mo')

for ticker in tickers:
    trend = moving_average_trend(dat.loc[:, ('Close', ticker)], 5)
    rsi_trend = rsi(dat.loc[:, ('Close', ticker)], 14)

    signal = check_buy_signal(trend, rsi_trend)
    if signal:
        print(f"{ticker} СИГНАЛ НА КУПІВЛЮ")
    else:
        print(f"{ticker} немає сигналу")