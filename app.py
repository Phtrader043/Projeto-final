import streamlit as st
from signal_engine import gerar_sinal
from utils import salvar_sinal, exibir_historico
import time

st.set_page_config(page_title="Indicador Trader IA", layout="wide")

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://i.imgur.com/FWzP6KR.jpg');
        background-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📈 Indicador Trader IA - Cripto e Forex")

modo = st.selectbox("Escolha o modo de operação:", ["Conservador", "Agressivo"])

ativar = st.toggle("🚀 Ativar IA (Geração Automática de Sinais)")

if ativar:
    with st.spinner("🔍 Buscando sinais..."):
        while ativar:
            sinal = gerar_sinal(modo)
            if sinal:
                st.success(f"✅ Sinal Gerado: {sinal}")
                salvar_sinal(sinal)
            else:
                st.warning("⚠️ Nenhum sinal confiável encontrado no momento.")
            time.sleep(60)  # Checa a cada minuto

exibir_historico()
