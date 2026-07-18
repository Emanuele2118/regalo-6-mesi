import streamlit as st
from datetime import datetime

# Configurazione Pagina
st.set_page_config(page_title="6 Mesi di Noi", layout="centered")

# CSS per lo stile a scorrimento
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
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    h1, h2 { color: #ffffff !important; text-align: center; margin-top: 30px; }
    img { border-radius: 20px; width: 100% !important; margin: 10px 0; }
    </style>
""", unsafe_allow_html=True)

# Logica Dati
start = datetime(2026, 1, 18, 23, 12, 0)
now = datetime.now()
diff = now - start
mesi = (now.year - start.year) * 12 + (now.month - start.month)
if now.day < start.day: mesi -= 1

# Struttura a scorrimento (senza tab)
st.markdown("<h1>6 Mesi di Noi</h1>", unsafe_allow_html=True)
st.markdown("<div class='card'>Emanuele & Mia</div>", unsafe_allow_html=True)

st.header("Il nostro tempo")
st.markdown(f"<div class='card'><h3>{mesi} Mesi</h3></div>", unsafe_allow_html=True)
st.markdown(f"<div class='card'><h3>{diff.days} Giorni</h3></div>", unsafe_allow_html=True)
st.markdown(f"<div class='card'><h3>{int(diff.total_seconds()):,} Secondi</h3></div>", unsafe_allow_html=True)

st.header("I nostri momenti")
st.image("https://i.ibb.co/67spRrzZ/IMG-20260718-151122.jpg")
st.image("https://i.ibb.co/zVJ7tzK5/IMG-20260718-151147.jpg")

st.header("Promessa")
st.markdown("<div class='card'><h1>Giuro sulla tua vita</h1><h2>❤️ ∞</h2></div>", unsafe_allow_html=True)

st.header("Auguri")
st.image("https://i.ibb.co/Df9CBr17/IMG-20260718-151221.jpg")
st.balloons()
