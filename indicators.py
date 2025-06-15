import pandas as pd
import numpy as np

def analisar_indicadores(df):
    df['EMA_10'] = df['close'].ewm(span=10, adjust=False).mean()
    df['EMA_20'] = df['close'].ewm(span=20, adjust=False).mean()
    df['RSI'] = calcular_rsi(df['close'], 14)
    df['MACD'] = df['EMA_10'] - df['EMA_20']

    condicao_compra = (df['EMA_10'].iloc[-1] > df['EMA_20'].iloc[-1]) and (df['RSI'].iloc[-1] < 70)
    condicao_venda = (df['EMA_10'].iloc[-1] < df['EMA_20'].iloc[-1]) and (df['RSI'].iloc[-1] > 30)

    if condicao_compra:
        return "COMPRA"
    elif condicao_venda:
        return "VENDA"
    else:
        return "NEUTRO"

def calcular_rsi(series, period=14):
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = -1 * delta.clip(upper=0)
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
