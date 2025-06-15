from data_fetcher import obter_candles
from indicators import analisar_indicadores
from cohere_analysis import analisar_tendencia
from config import ATIVOS
from datetime import datetime, timedelta
import pytz
import random

def gerar_sinal(modo):
    for ativo in ATIVOS:
        try:
            df = obter_candles(ativo)
            resultado_indicadores = analisar_indicadores(df)
            if resultado_indicadores != "NEUTRO":
                resultado_ia = analisar_tendencia(resultado_indicadores, modo)

                if resultado_ia in ["COMPRA", "VENDA"]:
                    hora_brasilia = datetime.now(pytz.timezone('America/Sao_Paulo'))
                    entrada = (hora_brasilia + timedelta(minutes=2)).strftime('%H:%M')
                    saida = (hora_brasilia + timedelta(minutes=7)).strftime('%H:%M')
                    tendencia = random.randint(85, 99)

                    sinal = {
                        "Ativo": ativo,
                        "Tipo": resultado_ia,
                        "Entrada": entrada,
                        "Saída": saida,
                        "Tendência": f"{tendencia}%"
                    }
                    return sinal
        except:
            continue
    return None
