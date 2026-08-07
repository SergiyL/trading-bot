def check_buy_signal(trend, rsi_values):
    last_trend = trend.iloc[-1]
    last_rsi = rsi_values.iloc[-1]
    
    return last_trend and last_rsi < 30