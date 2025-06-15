import requests
import pandas as pd
from config import TWELVEDATA_API_KEY

def obter_candles(ativo):
    url = f"https://api.twelvedata.com/time_series"
    params = {
        'symbol': ativo,
        'interval': '1min',
        'outputsize': 20,
        'apikey': TWELVEDATA_API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data['values'])
    df = df.astype(float)
    return df

def obter_preco_atual(ativo):
    url = f"https://min-api.cryptocompare.com/data/price"
    params = {'fsym': ativo.split('/')[0], 'tsyms': ativo.split('/')[1]}
    response = requests.get(url, params=params)
    return response.json()[ativo.split('/')[1]]
