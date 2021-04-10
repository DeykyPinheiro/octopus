import numpy as np
import pandas as pd

# receives a series or array, return a series of the average of n periods
def moving_average_rolling(data, periods=20):
    data = pd.Series(data, name=f'mean_{periods}')    
    s = data.rolling(window=periods).mean()
    return s

# receives a series or array, return a series of the exponential average of n periods
def exponential_moving_average_rolling(data, periods=10):
    data = pd.Series(data, , name=f'mme_{periods}')
    s = pd.Series(pd.core.window.ExponentialMovingWindow(data, periods).mean())
    return s

# Recebe um Serie, retorna um df com a linha macd e o sinal
def macd(df, curta=12, longa=26, sinal=9):
    a = media_exponencial_deslizante(df, curta)
    b = media_exponencial_deslizante(df, longa)
    df_macd = pd.DataFrame(a.values - b.values)
    df_macd.columns = ['macd']
    df_macd[f'mme_macd_{sinal}'] = media_exponencial_deslizante(df_macd, sinal)
    return  df_macd

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