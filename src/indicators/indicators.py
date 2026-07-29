def moving_average_trend(prices, window):
    roll_mean = prices.rolling(window).mean().dropna()
    prices_clean = prices.loc[roll_mean.index]
    trend = prices_clean > roll_mean
    return trend

def rsi(prices, window):
    changes = prices.diff()
    gains = changes.clip(lower=0)
    losses = -changes.clip(upper=0)
    avg_gain = gains.rolling(window).mean()
    avg_loss = losses.rolling(window).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi