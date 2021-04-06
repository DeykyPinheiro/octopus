import numpy as np
import pandas as pd

# medias moveis, padrao 20
def medias_moveis(df, periodos=20):
    df[f'mean_{periodos}'] = df['Close'].rolling(window=periodos).mean()


# retorna um DataFrame, para concatenar ao df, original
def media_exponencial(df, periodos=10):
    df_mme = pd.DataFrame(pd.core.window.ExponentialMovingWindow(df, periodos).mean())
    df_mme.columns = [f'mme_{periodos}']
    return df_mme

# Recebe um Serie
def macd_df(df):
    a = media_exponencial(df, 12)
    b = media_exponencial(df, 26)
    df_macd = pd.DataFrame(a.values - b.values)
    df_macd.columns = ['macd']
    df_macd['mme_macd_9'] = media_exponencial(df_macd, 9)
    return  df_macd