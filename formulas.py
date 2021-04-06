import numpy as np
import pandas as pd

#medias moveis, padrao 20
def medias_moveis(df, periodos=20):
    df[f'mean_{periodos}'] = df['Close'].rolling(window=periodos).mean()

