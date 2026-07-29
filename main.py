from src.data.fetcher import get_prices
from src.indicators.indicators import moving_average_trend, rsi
tickers = ['GOOGL', 'META', 'NFLX']
dat = get_prices(tickers, '1mo')

for ticker in tickers:
    trend = moving_average_trend(dat.loc[:, ('Close', ticker)], 5)
    rsi_trend = rsi(dat.loc[:, ('Close', ticker)], 14)
    print(f"\n{ticker}:")
    print(trend)
    print(rsi_trend)
