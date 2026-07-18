import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="6 Mesi di Noi", layout="centered")

# CSS: Sfondo rosa, scritte rosso scuro, font elegante, SCHERMO FISSO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');
    
    /* Blocca lo scroll */
    body, html, .stApp { 
        background-color: #ffdde1; 
        overflow: hidden !important; 
        height: 100vh;
    }
    
    h1, .subtitle { 
        font-family: 'Playfair Display', serif; 
        color: #8b0000 !important; 
        text-align: center; 
        margin-bottom: 5px;
    }
    .timer-box { 
        background-color: #ffffff; 
        padding: 10px; 
        border-radius: 15px; 
        text-align: center; 
        margin: 5px auto; 
        color: #8b0000; 
        font-family: 'Playfair Display', serif;
        font-size: 20px;
        font-weight: bold;
        border: 2px solid #8b0000;
        width: 80%;
    }
    </style>
""", unsafe_allow_html=True)

# Data di riferimento
start = datetime(2026, 1, 18, 23, 12, 0)
now = datetime.now()
delta = now - start

# Calcoli indipendenti
anni = (now.year - start.year) - ((now.month, now.day) < (start.month, start.day))
mesi_totali = (now.year - start.year) * 12 + (now.month - start.month) - (now.day < start.day)
settimane_totali = delta.days // 7
giorni_totali = delta.days
ore_totali = int(delta.total_seconds() // 3600)
secondi_totali = int(delta.total_seconds())

# Interfaccia
st.markdown("<h1>6 Mesi di Noi</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Emanuele & Mia, per sempre</div>", unsafe_allow_html=True)

# Timer Verticale
st.markdown(f"<div class='timer-box'>Anni: {anni}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='timer-box'>Mesi: {mesi_totali}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='timer-box'>Settimane: {settimane_totali}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='timer-box'>Giorni: {giorni_totali}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='timer-box'>Ore: {ore_totali}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='timer-box'>Secondi: {secondi_totali:,}</div>", unsafe_allow_html=True)

time.sleep(1)
st.rerun()
