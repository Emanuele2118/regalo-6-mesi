import streamlit as st
import time
from datetime import datetime

# Configurazione pagina
st.set_page_config(page_title="6 Mesi di Noi", layout="centered")

# CSS: Font, centratura e immagini grandi
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif !important; }
    
    .stApp { background: linear-gradient(180deg, #ffccd5 0%, #ff4d6d 100%); }
    .card { 
        background-color: rgba(255, 255, 255, 0.95); 
        padding: 25px; 
        border-radius: 25px; 
        text-align: center; 
        margin: 20px 0; 
        color: #d63384; 
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }
    h1, h2, h3 { color: #ffffff !important; text-align: center !important; margin-top: 20px; }
    img { border-radius: 20px; width: 100% !important; margin: 15px 0; display: block; margin-left: auto; margin-right: auto; }
    </style>
""", unsafe_allow_html=True)

# Logica Timer
start = datetime(2026, 1, 18, 23, 12, 0)
now = datetime.now()
diff = now - start
mesi = (now.year - start.year) * 12 + (now.month - start.month)
if now.day < start.day: mesi -= 1

# Interfaccia
st.markdown("<h1>6 Mesi di Noi</h1>", unsafe_allow_html=True)
st.markdown("<div class='card'>Emanuele & Mia</div>", unsafe_allow_html=True)

st.header("Il nostro tempo")
st.markdown(f"""
    <div class='card'>
        <h3>{mesi} Mesi</h3>
        <h3>{diff.days} Giorni</h3>
        <h3>{int(diff.total_seconds()):,} Secondi</h3>
    </div>
""", unsafe_allow_html=True)

st.header("I nostri momenti")
st.image("https://i.ibb.co/67spRrzZ/IMG-20260718-151122.jpg")
st.image("https://i.ibb.co/zVJ7tzK5/IMG-20260718-151147.jpg")

st.header("Promessa")
st.markdown("""
    <div class='card'>
        <h2>Noi per sempre</h2>
        <p style='font-size: 20px; font-weight: bold;'>Giuro sulla tua vita</p>
        <h1>❤️ ∞</h1>
    </div>
""", unsafe_allow_html=True)

st.header("Auguri")
st.image("https://i.ibb.co/Df9CBr17/IMG-20260718-151221.jpg")
st.balloons()

# Aggiornamento tempo reale (ogni secondo)
time.sleep(1)
st.rerun()
