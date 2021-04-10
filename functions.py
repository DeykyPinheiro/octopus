import numpy as np
import pandas as pd

# receives a series or array, return a series of the average of n periods
def moving_average_rolling(data, periods=20):
    data = pd.Series(data, name=f'mean_{periods}')    
    s = data.rolling(window=periods).mean()
    return s

# receives a series or array, return a series of the exponential average of n periods
def exponential_moving_average_rolling(data, periods=9):
    data = pd.Series(data, name=f'mme_{periods}')
    s = pd.Series(pd.core.window.ExponentialMovingWindow(data, periods).mean())
    return s

# receives a series or array,returns a DataFrame with macd and mme of n periods of the macd line
def macd(data, short=12, long=26, signal=9):

    data = pd.Series(data)
    a = exponential_moving_average_rolling(data, short)
    b = exponential_moving_average_rolling(data, long)
    
    macd = pd.Series(a.values - b.values, name='macd')
    mme = pd.DataFrame(exponential_moving_average_rolling(macd, periods=signal))
    
    df = pd.concat([macd, mme], axis=1)
    return  df

# receives a DataFrame with mandatory columns: High, Low, Close.
# returns a series with the ATR
def atr(data, periods=14):
    
    df = data.copy()
    high = df['High']
    low = df['Low']
    close = df['Close']

    df['tr0'] = abs(high - low)
    df['tr1'] = abs(high - close.shift(1))
    df['tr2'] = abs(low - close.shift(1))
    
    tr = df[['tr0', 'tr1', 'tr2']].max(1)
    atr = pd.Series(exponential_moving_average_rolling(tr, periods), name=f'atr')
    
    return atr