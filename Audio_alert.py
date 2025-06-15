from gtts import gTTS
import streamlit as st
import os

def alerta_sonoro(ativo):
    texto = f"ATENÇÃO SENHOR PEDRO, UM NOVO SINAL FOI IDENTIFICADO PARA {ativo}"
    tts = gTTS(text=texto, lang='pt-br')
    arquivo_audio = f"alerta_{ativo}.mp3"
    tts.save(arquivo_audio)

    with open(arquivo_audio, 'rb') as audio_file:
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format='audio/mp3')

    os.remove(arquivo_audio)
  
