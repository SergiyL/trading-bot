def moving_average_trend(prices, window):
    roll_mean = prices.rolling(window).mean().dropna()
    prices_clean = prices.loc[roll_mean.index]
    trend = prices_clean > roll_mean
    return trend
