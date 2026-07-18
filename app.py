import streamlit as st
import time
from datetime import datetime

# Configurazione semplice
st.set_page_config(page_title="6 Mesi", layout="centered")

# Stile: Sfondo a strisce Rosa/Rosso delicato
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #ffccd5 0%, #ff4d6d 100%);
    }
    h1, h2, h3, p, div { color: #ffffff !important; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

start = datetime(2026, 1, 18, 23, 12, 0)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Inizio", "Tempo", "Momenti", "Promessa", "Auguri"])

with tab1:
    st.title("6 Mesi di Noi")
    st.write("Emanuele & Mia")

with tab2:
    st.header("Il nostro tempo")
    placeholder = st.empty()
    while True:
        now = datetime.now()
        diff = now - start
        mesi = (now.year - start.year) * 12 + (now.month - start.month)
        if now.day < start.day: mesi -= 1
        
        with placeholder.container():
            st.metric("Mesi", mesi)
            st.metric("Giorni", diff.days)
            st.metric("Secondi", f"{int(diff.total_seconds()):,}")
        time.sleep(1)

with tab3:
    st.header("I nostri momenti")
    st.image("https://i.ibb.co/67spRrzZ/IMG-20260718-151122.jpg", use_container_width=True)
    st.image("https://i.ibb.co/zVJ7tzK5/IMG-20260718-151147.jpg", use_container_width=True)

with tab4:
    st.header("Giuro sulla tua vita")
    st.subheader("❤️ ∞")

with tab5:
    st.header("Auguri Mia!")
    st.image("https://i.ibb.co/Df9CBr17/IMG-20260718-151221.jpg", use_container_width=True)
    st.balloons()
