import streamlit as st
import time
from datetime import datetime

# Configurazione
st.set_page_config(page_title="6 Mesi di Noi", layout="wide")

# CSS: Immagini a larghezza piena e timer elegante
st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #ffccd5 0%, #ff4d6d 100%); }
    .timer-card { 
        background-color: rgba(255, 255, 255, 0.95); 
        padding: 25px; 
        border-radius: 20px; 
        text-align: center; 
        margin: 20px auto; 
        color: #d63384; 
        font-weight: bold; 
        font-size: 18px;
        max-width: 500px;
    }
    .text-card { 
        background-color: rgba(255, 255, 255, 0.95); 
        padding: 15px; 
        border-radius: 0 0 20px 20px; 
        text-align: center; 
        margin-bottom: 30px; 
        color: #d63384; 
        font-weight: bold;
        max-width: 100%;
    }
    h1 { color: #ffffff !important; text-align: center; padding-top: 20px; }
    img { width: 100% !important; border-radius: 20px 20px 0 0; display: block; }
    </style>
""", unsafe_allow_html=True)

# Calcolo preciso del tempo
start = datetime(2026, 1, 18, 23, 12, 0)
now = datetime.now()
delta = now - start

anni = delta.days // 365
mesi = (delta.days % 365) // 30
settimane = (delta.days % 365 % 30) // 7
giorni = delta.days % 365 % 30 % 7
ore = delta.seconds // 3600
secondi = (delta.seconds % 3600) % 60

# Interfaccia
st.markdown("<h1>6 Mesi di Noi</h1>", unsafe_allow_html=True)

st.markdown(f"""
    <div class='timer-card'>
        Anni: {anni} | Mesi: {mesi} | Settimane: {settimane}<br>
        Giorni: {giorni} | Ore: {ore} | Secondi: {secondi}
    </div>
""", unsafe_allow_html=True)

# Immagini a piena larghezza
st.image("https://i.ibb.co/67spRrzZ/IMG-20260718-151122.jpg")
st.markdown("<div class='text-card'>Noi per sempre</div>", unsafe_allow_html=True)

st.image("https://i.ibb.co/zVJ7tzK5/IMG-20260718-151147.jpg")
st.markdown("<div class='text-card'>Giuro sulla tua vita</div>", unsafe_allow_html=True)

# Aggiornamento dinamico
time.sleep(1)
st.rerun()
