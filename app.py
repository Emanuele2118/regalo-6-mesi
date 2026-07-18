import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="6 Mesi di Noi", page_icon="❤️")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Inizio", "Il Nostro Tempo", "Momenti", "Promessa", "Auguri"])

with tab1:
    st.title("6 Mesi di Noi ❤️")
    st.write("Ogni secondo è stato un regalo.")

with tab2:
    st.header("Il nostro tempo insieme")
    placeholder = st.empty()
    start_date = datetime(2026, 1, 18, 23, 12, 0)
    
    while True:
        now = datetime.now()
        diff = now - start_date
        
        # Calcolo Mesi (approssimato)
        mesi = (now.year - start_date.year) * 12 + (now.month - start_date.month)
        if now.day < start_date.day: mesi -= 1
        
        # Calcolo Giorni (giorni passati dall'ultimo mese compiuto)
        giorni = (now - datetime(now.year, now.month, start_date.day)).days
        if giorni < 0: giorni = 0
            
        # Calcolo Secondi totali della giornata corrente
        secondi_di_oggi = now.hour * 3600 + now.minute * 60 + now.second
        
        with placeholder.container():
            st.metric("Mesi passati", f"{mesi} mesi")
            st.metric("Giorni extra", f"{giorni} giorni")
            st.metric("Secondi da inizio giornata", f"{secondi_di_oggi:,}")
        
        time.sleep(1)

with tab3:
    st.header("I nostri momenti")
    st.image("https://i.ibb.co/67spRrzZ/IMG-20260718-151122.jpg")
    st.image("https://i.ibb.co/zVJ7tzK5/IMG-20260718-151147.jpg")

with tab4:
    st.header("Giuro sulla tua vita")
    st.write("### ❤️ ∞")
    st.write("## Noi, per sempre")

with tab5:
    st.header("Auguri bimba mia")
    st.image("https://i.ibb.co/Df9CBr17/IMG-20260718-151221.jpg")
    st.balloons()
