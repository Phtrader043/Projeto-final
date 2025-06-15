import streamlit as st
import time
from signal_engine import gerar_sinal
from utils import exibir_historico, salvar_historico
from audio_alert import alerta_sonoro

# Configuração da página
st.set_page_config(
    page_title="Indicador GPT 1.0 - Equipe PHTrader",
    layout="wide",
    page_icon="💹"
)

st.title("💹 Indicador GPT 1.0 - Equipe PHTrader")
st.subheader("Análise Cripto & Forex em tempo real com IA + Indicadores")
st.markdown("---")

# Sidebar para configuração
st.sidebar.title("Configurações de Análise")

# Seleção de modo
modo = st.sidebar.radio(
    "Escolha o modo de operação:",
    ('Conservador', 'Agressivo')
)

# Botão para ativar IA
ativar_ia = st.sidebar.toggle("🚀 Ativar IA")

st.sidebar.markdown("---")
st.sidebar.subheader("🔔 Histórico de Sinais")

# Exibir histórico no sidebar
exibir_historico()

st.markdown("---")
st.subheader("🧠 Monitoramento em Tempo Real")

# Loop enquanto IA está ativada
if ativar_ia:
    status = st.empty()
    while ativar_ia:
        status.info("🔍 Buscando novos sinais...")

        sinal = gerar_sinal(modo)

        if sinal:
            st.success(f"""### ✅ Novo Sinal Detectado:
- **Ativo:** {sinal['ativo']}
- **Tipo:** {sinal['tipo']}
- **Entrada:** {sinal['entrada']}
- **Saída:** {sinal['saida']}
- **Tendência:** {sinal['tendencia']}
""")

            alerta_sonoro(sinal['ativo'])  # 🔥 Alerta Sonoro
            salvar_historico(sinal)

        else:
            st.warning("🚫 Nenhum sinal identificado no momento.")

        time.sleep(60)  # Espera 60 segundos antes de buscar novamente
        ativar_ia = st.sidebar.toggle("🚀 Ativar IA", value=True)  # Mantém o botão ativo

else:
    st.info("🟢 IA Desativada. Ative para começar a gerar sinais.")
    
