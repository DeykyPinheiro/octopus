import numpy as np
import pandas as pd

#medias moveis, padrao 20
def medias_moveis(df, periodos=20):
    df[f'mean_{periodos}'] = df['Close'].rolling(window=periodos).mean()

def media_exponencial(df, periodos=10):
    df[f'mme_{periodos}'] = pd.core.window.ExponentialMovingWindow(df['Close'], periodos).mean()