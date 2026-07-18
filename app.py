import streamlit as st
from datetime import datetime

# Configurazione Pagina
st.set_page_config(page_title="6 Mesi di Noi", layout="centered")

# CSS Avanzato per centratura e visibilità forzata
st.markdown("""
    <style>
    .stApp { background: linear-gradient(180deg, #ff9aa2 0%, #ff4d6d 100%); }
    .card { background-color: rgba(255, 255, 255, 0.9); padding: 20px; border-radius: 20px; text-align: center; margin: 10px; color: #d63384; font-weight: bold; }
    h1, h2, h3 { color: #ffffff !important; text-align: center !important; }
    .stImage { display: flex; justify-content: center; }
    img { border-radius: 15px; width: 90% !important; margin: 0 auto; }
    </style>
""", unsafe_allow_html=True)

# Logica Dati
start = datetime(2026, 1, 18, 23, 12, 0)
now = datetime.now()
diff = now - start
mesi = (now.year - start.year) * 12 + (now.month - start.month)
if now.day < start.day: mesi -= 1

# Struttura Tab
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Inizio", "Tempo", "Momenti", "Promessa", "Auguri"])

with tab1:
    st.markdown("<h1>6 Mesi di Noi</h1><div class='card'>Emanuele & Mia</div>", unsafe_allow_html=True)

with tab2:
    st.header("Il nostro tempo")
    st.markdown(f"<div class='card'>Mesi<br><h2>{mesi}</h2></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='card'>Giorni<br><h2>{diff.days}</h2></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='card'>Secondi<br><h2>{int(diff.total_seconds()):,}</h2></div>", unsafe_allow_html=True)

with tab3:
    st.header("I nostri momenti")
    st.image("https://i.ibb.co/67spRrzZ/IMG-20260718-151122.jpg")
    st.image("https://i.ibb.co/zVJ7tzK5/IMG-20260718-151147.jpg")

with tab4:
    st.header("Giuro sulla tua vita")
    st.markdown("<div class='card'><h1>❤️ ∞</h1></div>", unsafe_allow_html=True)

with tab5:
    st.header("Auguri Mia!")
    st.image("https://i.ibb.co/Df9CBr17/IMG-20260718-151221.jpg")
    st.balloons()
