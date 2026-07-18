import streamlit as st
import time
from datetime import datetime

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="6 Mesi", layout="centered")

# --- CSS FORZATO PER LEGGIBILITÀ ---
st.markdown("""
    <style>
    /* Forziamo il testo a essere nero ovunque */
    .stApp, h1, h2, h3, p, div { color: #000000 !important; }
    
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 20px;
        border: 2px solid #ff0040;
        margin: 10px 0;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

start = datetime(2026, 1, 18, 23, 12, 0)

# --- LOGICA ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["❤️", "⏳", "📸", "📜", "✨"])

with tab1:
    st.markdown("<div class='card'><h1>6 Mesi di Noi</h1><p>Emanuele & Mia</p></div>", unsafe_allow_html=True)

with tab2:
    st.header("Il nostro tempo")
    placeholder = st.empty()
    while True:
        now = datetime.now()
        diff = now - start
        mesi = (now.year - start.year) * 12 + (now.month - start.month)
        if now.day < start.day: mesi -= 1
        
        with placeholder.container():
            st.markdown(f"<div class='card'><h3>{mesi} Mesi</h3></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='card'><h3>{diff.days} Giorni</h3></div>", unsafe_allow_html=True)
            st.markdown(f"<div class='card'><h3>{int(diff.total_seconds()):,} Secondi</h3></div>", unsafe_allow_html=True)
        time.sleep(1)

with tab3:
    st.image("https://i.ibb.co/67spRrzZ/IMG-20260718-151122.jpg")
    st.image("https://i.ibb.co/zVJ7tzK5/IMG-20260718-151147.jpg")

with tab4:
    st.markdown("<div class='card'><h2>Giuro sulla tua vita</h2><h1>❤️ ∞</h1></div>", unsafe_allow_html=True)

with tab5:
    st.header("Auguri Mia!")
    st.image("https://i.ibb.co/Df9CBr17/IMG-20260718-151221.jpg")
    st.balloons()
