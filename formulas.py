import numpy as np

#medias moveis, padrao 20
def medias_moveis(df, periodos=20):
    df[f'mean_{periodos}'] = df['Close'].rolling(window=20).mean()

