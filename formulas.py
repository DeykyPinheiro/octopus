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

# receives a series or array,returns a DataFrame, with macd and mme of n periods of the macd line
def macd(data, short=12, long=26, signal=9):

    data = pd.Series(data)
    a = exponential_moving_average_rolling(data, short)
    b = exponential_moving_average_rolling(data, long)
    
    macd = pd.Series(a.values - b.values, name='macd')
    mme = pd.DataFrame(exponential_moving_average_rolling(macd, periods=signal))
    
    df = pd.concat([macd, mme], axis=1)
    return  df

# Recebe um df e os periodos da media exponencial, e os periodos, e devolve um df com o ATR
# recebe apenas no padrao 'High', 'Low', 'Close'
def atr(df, periodos=14):
    
    data = df.copy()
    high = data['High']
    low = data['Low']
    close = data['Close']

    data['tr0'] = abs(high - low)
    data['tr1'] = abs(high - close.shift(1))
    data['tr2'] = abs(low - close.shift(1))
    
    tr = data[['tr0', 'tr1', 'tr2']].max(1)
    atr = media_exponencial_deslizante(tr, periodos)
    
    return atr