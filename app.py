import streamlit as st
import time
from datetime import datetime

# Configurazione base
st.set_page_config(page_title="6 Mesi", layout="centered")

# CSS: Sfondo rosa/rosso, testo bianco, immagini grandi e centrate
st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #ffccd5 0%, #ff4d6d 100%); }
    .card { 
        background-color: rgba(255, 255, 255, 0.9); 
        padding: 20px; 
        border-radius: 20px; 
        text-align: center; 
        margin: 15px 0; 
        color: #d63384;
        font-weight: bold;
        font-size: 20px;
    }
    h1 { color: #ffffff !important; text-align: center; }
    img { border-radius: 15px; width: 100% !important; margin: 10px auto; display: block; }
    </style>
""", unsafe_allow_html=True)

# Logica Timer
start = datetime(2026, 1, 18, 23, 12, 0)

# Interfaccia
st.markdown("<h1>6 Mesi di Noi</h1>", unsafe_allow_html=True)

# Timer (aggiornato in tempo reale)
now = datetime.now()
diff = now - start
mesi = (now.year - start.year) * 12 + (now.month - start.month)
if now.day < start.day: mesi -= 1

st.markdown(f"""
    <div class='card'>
        Mesi: {mesi}<br>
        Giorni: {diff.days}<br>
        Secondi: {int(diff.total_seconds()):,}
    </div>
""", unsafe_allow_html=True)

# Foto con didascalie
st.image("https://i.ibb.co/67spRrzZ/IMG-20260718-151122.jpg")
st.markdown("<div class='card'>Noi per sempre</div>", unsafe_allow_html=True)

st.image("https://i.ibb.co/zVJ7tzK5/IMG-20260718-151147.jpg")
st.markdown("<div class='card'>Giuro sulla tua vita</div>", unsafe_allow_html=True)

# Aggiornamento automatico
time.sleep(1)
st.rerun()
