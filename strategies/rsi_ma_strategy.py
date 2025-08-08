def generate_signals(df):
    signals = []
    position = False
    for i in range(50, len(df)):
        rsi = df['RSI'].iloc[i]
        dma20 = df['20DMA'].iloc[i]
        dma50 = df['50DMA'].iloc[i]

        if not position and rsi < 30 and dma20 > dma50:
            signals.append(('Buy', df.index[i], df['Close'].iloc[i]))
            position = True
        elif position and (rsi > 70 or dma20 < dma50):
            signals.append(('Sell', df.index[i], df['Close'].iloc[i]))
            position = False
    return signals