import streamlit as st
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="6 Mesi di Noi", layout="centered")

# CSS: Stile pulito
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');
    .stApp { background-color: #ffdde1 !important; }
    h1 { font-family: 'Playfair Display', serif; color: #8b0000 !important; text-align: center; font-size: 2.2rem !important; margin: 10px 0 !important; }
    .subtitle { font-family: 'Playfair Display', serif; color: #8b0000 !important; text-align: center; font-size: 1.3rem !important; margin-bottom: 15px !important; }
    .timer-box { background-color: #ffffff; padding: 12px !important; border-radius: 12px; text-align: center; margin: 6px auto !important; color: #8b0000; font-family: 'Playfair Display', serif; font-size: 1.5rem !important; font-weight: bold; border: 2px solid #8b0000; width: 85%; }
    </style>
""", unsafe_allow_html=True)

# Data di riferimento
start = datetime(2026, 1, 18, 23, 12, 0)
now = datetime.now()

# Calcolo preciso con relativedelta
diff = relativedelta(now, start)

# Conteggi per riga (calcolando il totale di ciascuna unità trascorso)
# Usiamo il totale delle unità per ogni riga, così ogni numero è indipendente
delta_total = now - start
tot_anni = diff.years
tot_mesi = (now.year - start.year) * 12 + now.month - start.month - (1 if now.day < start.day or (now.day == start.day and now.hour < start.hour) else 0)
tot_settimane = delta_total.days // 7
tot_giorni = delta_total.days
tot_ore = int(delta_total.total_seconds() // 3600)
tot_secondi = int(delta_total.total_seconds())

# Interfaccia
st.markdown("<h1>Il Nostro Tempo</h1>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Emanuele & Mia, per sempre</div>", unsafe_allow_html=True)

st.markdown(f"<div class='timer-box'>Anni: {tot_anni}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='timer-box'>Mesi: {tot_mesi}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='timer-box'>Settimane: {tot_settimane}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='timer-box'>Giorni: {tot_giorni}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='timer-box'>Ore: {tot_ore}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='timer-box'>Secondi: {tot_secondi:,}</div>", unsafe_allow_html=True)

time.sleep(1)
st.rerun()
