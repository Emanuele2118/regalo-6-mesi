import streamlit as st
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

st.set_page_config(page_title="6 Mesi di Noi", layout="centered")

# CSS: Sfondo con cuori, font elegante e immagini a larghezza piena
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');
    .stApp { 
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
        background-image: radial-gradient(white 1px, transparent 1px);
        background-size: 30px 30px;
    }
    h1, h2, .title-text { 
        font-family: 'Playfair Display', serif; 
        color: #d63384 !important; 
        text-align: center; 
        text-shadow: 1px 1px 2px white;
    }
    .card { 
        background-color: rgba(255, 255, 255, 0.85); 
        padding: 20px; 
        border-radius: 20px; 
        text-align: center; 
        margin: 15px 0; 
        color: #b5179e; 
        font-weight: bold;
        border: 2px solid #ff758f;
    }
    img { width: 100% !important; border-radius: 20px; margin: 10px 0; }
    </style>
""", unsafe_allow_html=True)

# Logica Tempo
start = datetime(2026, 1, 18, 23, 12, 0)
now = datetime.now()
diff = relativedelta(now, start)

# Interfaccia
st.markdown("<h1>6 Mesi di Noi</h1>", unsafe_allow_html=True)
st.markdown("<div class='title-text'>Emanuele & Mia, per sempre</div>", unsafe_allow_html=True)

st.markdown(f"""
    <div class='card'>
        Anni: {diff.years} | Mesi: {diff.months} | Settimane: {diff.weeks}<br>
        Giorni: {diff.days} | Ore: {diff.hours} | Secondi: {diff.seconds}
    </div>
""", unsafe_allow_html=True)

st.image("https://i.ibb.co/67spRrzZ/IMG-20260718-151122.jpg")
st.markdown("<div class='card'>Noi per sempre</div>", unsafe_allow_html=True)

st.image("https://i.ibb.co/zVJ7tzK5/IMG-20260718-151147.jpg")
st.markdown("<div class='card'>Giuro sulla tua vita</div>", unsafe_allow_html=True)

time.sleep(1)
st.rerun()
