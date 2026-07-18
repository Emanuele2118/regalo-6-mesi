import streamlit as st
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="6 Mesi di Noi", layout="centered")

# CSS: Sfondo rosa, scritte rosso scuro, font elegante
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');
    .stApp { background-color: #ffdde1; }
    h1, .subtitle { 
        font-family: 'Playfair Display', serif; 
        color: #8b0000 !important; 
        text-align: center; 
    }
    .timer-box { 
        background-color: #ffffff; 
        padding: 15px; 
        border-radius: 15px; 
        text-align: center; 
        margin: 10px 0; 
        color: #8b0000; 
        font-family: 'Playfair Display', serif;
        font-size: 22px;
        font-weight: bold;
        border: 2px solid #8b0000;
    }
    </style>
""", unsafe_allow_html=True)

# Logica
start = datetime(2026, 1, 18, 23, 12, 0)
now = datetime.now()
diff = relativedelta(now, start)

# Interfaccia
st.markdown("<h1>6 Mesi di Noi</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Emanuele & Mia, per sempre</div>", unsafe_allow_html=True)

# Timer Verticale
st.markdown(f"<div class='timer-box'>Anni: {diff.years}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='timer-box'>Mesi: {diff.months}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='timer-box'>Settimane: {diff.weeks}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='timer-box'>Giorni: {diff.days}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='timer-box'>Ore: {diff.hours}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='timer-box'>Secondi: {diff.seconds}</div>", unsafe_allow_html=True)

time.sleep(1)
st.rerun()
