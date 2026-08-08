def ma_rsi(trend, rsi_values, rsi_threshold=30, mode='reversal'):
    if mode == 'reversal':
        return trend & (rsi_values < rsi_threshold)
    elif mode == 'confirmation':
        return trend & (rsi_values > rsi_threshold)
    else:
        raise ValueError(f"Невідомий mode: {mode}")