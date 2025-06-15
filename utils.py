import streamlit as st
import pandas as pd

def salvar_sinal(sinal):
    try:
        df = pd.read_csv('historico_sinais.csv')
    except:
        df = pd.DataFrame()

    novo = pd.DataFrame([sinal])
    df = pd.concat([df, novo], ignore_index=True)
    df.to_csv('historico_sinais.csv', index=False)

def exibir_historico():
    try:
        df = pd.read_csv('historico_sinais.csv')
        st.subheader("Histórico de Sinais")
        st.table(df.tail(10))
    except:
        st.info("Nenhum sinal gerado ainda.")
