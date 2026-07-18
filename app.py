import streamlit as st
import time
from datetime import datetime

# Configurazione stile pagina
st.set_page_config(page_title="6 Mesi di Noi", page_icon="❤️")

# Stile CSS
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f5;
        background-image: radial-gradient(#ffb6c1 1px, transparent 1px);
        background-size: 20px 20px;
    }
    h1, h2 { color: #d63384; text-align: center; }
    .big-font { font-size:24px !important; color: #555; text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Creazione delle 5 tab
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Inizio", "Il Nostro Tempo", "Momenti", "Promessa", "Auguri"])

# SCHERMATA 1
with tab1:
    st.markdown("<h1>6 Mesi di Noi</h1>", unsafe_allow_html=True)
    st.markdown("<p class='big-font'>Ogni secondo è stato un regalo.</p>", unsafe_allow_html=True)

# SCHERMATA 2: Timer
with tab2:
    st.header("Il nostro tempo insieme")
    placeholder = st.empty()
    start_date = datetime(2026, 1, 18, 23, 12, 0)
    
    # Ciclo per aggiornare il timer
    for _ in range(10000):
        now = datetime.now()
        diff = now - start_date
        mesi = (now.year - start_date.year) * 12 + (now.month - start_date.month)
        if now.day < start_date.day: mesi -= 1
        
        ore = diff.seconds // 3600
        minuti = (diff.seconds % 3600) // 60
        secondi = diff.seconds % 60
        millis = now.microsecond // 1000
        
        with placeholder.container():
            st.markdown(f"<h2>{mesi} Mesi</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2>{diff.days % 30} Giorni</h2>", unsafe_allow_html=True)
            st.markdown(f"<h2>{ore:02}:{minuti:02}:{secondi:02}.{millis:03}</h2>", unsafe_allow_html=True)
        time.sleep(0.1)

# SCHERMATA 3: Le tue foto
with tab3:
    st.header("I nostri migliori momenti insieme")
    st.image("https://i.ibb.co/67spRrzZ/IMG-20260718-151122.jpg", use_column_width=True)
    st.image("https://i.ibb.co/zVJ7tzK5/IMG-20260718-151147.jpg", use_column_width=True)

# SCHERMATA 4
with tab4:
    st.markdown("<h1 style='font-size: 40px;'>Giuro sulla tua vita</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size: 60px;'>❤️ ∞</h2>", unsafe_allow_html=True)
    st.markdown("<h2>Noi, per sempre</h2>", unsafe_allow_html=True)

# SCHERMATA 5
with tab5:
    st.header("Auguri bimba mia")
    st.image("https://i.ibb.co/Df9CBr17/IMG-20260718-151221.jpg", use_column_width=True)
    st.balloons()
