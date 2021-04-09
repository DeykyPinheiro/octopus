import numpy as np
import pandas as pd

# medias simples, desliza em uma serie/df um determindado numero de periodoso padrao 20
def medias_delizantes(serie, periodos=20):
    df = pd.DataFrame(serie.rolling(window=periodos).mean())
    df.columns = [f'mean_{periodos}']
    return df


# retorna um DataFrame, para concatenar ao df, original
def media_exponencial_deslizante(df, periodos=10):
    df_mme = pd.DataFrame(pd.core.window.ExponentialMovingWindow(df, periodos).mean())
    df_mme.columns = [f'mme_{periodos}']
    return df_mme

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