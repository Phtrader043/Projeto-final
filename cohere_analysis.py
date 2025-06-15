import cohere
from config import COHERE_API_KEY

co = cohere.Client(COHERE_API_KEY)

def analisar_tendencia(dados, modo):
    prompt = (
        f"Você é um analista profissional de mercados Forex e Cripto. "
        f"Analise os seguintes dados de indicadores: {dados}. "
        f"O modo atual é {modo}. Retorne apenas COMPRA, VENDA ou NEUTRO."
    )
    resposta = co.generate(
        model='command',
        prompt=prompt,
        max_tokens=50
    )
    return resposta.generations[0].text.strip()
