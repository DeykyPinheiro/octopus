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

# Recebe um Serie, retorna um df com a linha macd e o sinal
def macd_df(df, curta=12, longa=26, sinal=9):
    a = media_exponencial(df, curta)
    b = media_exponencial(df, longa)
    df_macd = pd.DataFrame(a.values - b.values)
    df_macd.columns = ['macd']
    df_macd[f'mme_macd_{sinal}'] = media_exponencial(df_macd, sinal)
    return  df_macd