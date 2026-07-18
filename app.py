import streamlit as st
import time
from datetime import datetime

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="6 Mesi di Noi - Il nostro amore", page_icon="❤️", layout="centered")

# --- STILE GRAFICO PERSONALIZZATO (CSS) ---
# Questo CSS crea uno sfondo elegante, font eleganti e contenitori con ombre e bordi morbidi.
st.markdown("""
    <style>
    /* Sfondo generale con gradiente romantico */
    .stApp {
        background: linear-gradient(135deg, #fff5f8 0%, #ffffff 100%);
    }
    
    /* Font per titoli e testo */
    h1, h2, h3 {
        font-family: 'Georgia', serif; /* Font elegante per i titoli */
        color: #5d275c; /* Bordeaux scuro per il titolo principale */
        text-align: center;
        font-weight: 700;
    }
    p, li, div {
        font-family: 'Arial', sans-serif;
        color: #4a4a4a;
    }
    
    /* Contenitore principale per le sezioni (card) */
    .custom-container {
        background-color: rgba(255, 255, 255, 0.85); /* Sfondo bianco semi-trasparente */
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08); /* Ombra morbida */
        border: 1px solid #ffe6f0;
        margin-bottom: 20px;
    }
    
    /* Stile per il timer */
    .timer-box {
        text-align: center;
        background-color: #fff0f5; /* Rosa molto chiaro */
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #d63384; /* Bordo rosa acceso */
        margin-bottom: 15px;
    }
    .timer-label {
        font-size: 18px;
        color: #d63384;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .timer-value {
        font-size: 48px;
        color: #4a4a4a;
        font-weight: 900;
        margin-top: 5px;
    }
    
    /* Titolo della pagina personalizzato */
    .main-title {
        font-size: 60px !important;
        margin-bottom: 10px;
    }
    .subtitle {
        font-size: 22px !important;
        color: #555 !important;
        font-weight: normal !important;
        font-style: italic;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# --- INIZIALIZZAZIONE DATA ---
# Data e ora esatta di riferimento
start_date = datetime(2026, 1, 18, 23, 12, 0)

# --- CREAZIONE TABS ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["❤️ Inizio", "⏳ Il Nostro Tempo", "📸 Momenti", "📜 Promessa", "✨ Auguri"])

# --- SCHERMATA 1: INIZIO ---
with tab1:
    st.markdown("<div class='custom-container'>", unsafe_allow_html=True)
    st.markdown("<h1 class='main-title'>6 Mesi di Noi</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Sei il regalo più bello che la vita potesse farmi. Emanuele ❤️ Ilenia</p>", unsafe_allow_html=True)
    # Aggiunta di un elemento visivo romantico
    st.image("https://i.ibb.co/3s8p9j98/IMG-20260718-151048.jpg", use_column_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCHERMATA 2: IL NOSTRO TEMPO (TIMER CORRETTO) ---
with tab2:
    st.markdown("<div class='custom-container'>", unsafe_allow_html=True)
    st.header("Il nostro tempo insieme")
    st.write("Un amore che cresce giorno dopo giorno, secondo dopo secondo.")
    
    placeholder = st.empty()
    
    while True:
        now = datetime.now()
        diff = now - start_date
        
        # Calcolo Mesi (basato sulla differenza di data grezza, semplificato ma preciso)
        # È un calcolo complesso. Usiamo una stima attendibile: mesi_tot = mesi da inizio anno + mesi interi
        mesi_tot = (now.year - start_date.year) * 12 + (now.month - start_date.month)
        if now.day < start_date.day: mesi_tot -= 1
        
        # Calcolo Giorni Totali (dalla data di inizio)
        giorni_tot = diff.days
        
        # Calcolo Secondi Totali (dalla data di inizio)
        secondi_tot = int(diff.total_seconds())
        
        with placeholder.container():
            # Blocco 1: Mesi
            st.markdown(f"""
                <div class='timer-box'>
                    <div class='timer-label'>📆 Abbiamo vissuto già</div>
                    <div class='timer-value'>{mesi_tot} <span style='font-size: 30px; color: #d63384;'>Mesi</span></div>
                    <span style='font-size: 40px;'>❤️</span>
                </div>
            """, unsafe_allow_html=True)
            
            # Blocco 2: Giorni
            st.markdown(f"""
                <div class='timer-box'>
                    <div class='timer-label'>☀️ Che corrispondono a</div>
                    <div class='timer-value'>{giorni_tot:,} <span style='font-size: 30px; color: #d63384;'>Giorni</span></div>
                    <span style='font-size: 40px;'>✨</span>
                </div>
            """, unsafe_allow_html=True)

            # Blocco 3: Secondi
            st.markdown(f"""
                <div class='timer-box'>
                    <div class='timer-label'>⏱️ E a ben</div>
                    <div class='timer-value'>{secondi_tot:,} <span style='font-size: 30px; color: #d63384;'>Secondi</span></div>
                     <span style='font-size: 40px;'>♾️</span>
                </div>
            """, unsafe_allow_html=True)
            
        time.sleep(1) # Aggiornamento ogni secondo
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCHERMATA 3: FOTO DEI MOMENTI ---
with tab3:
    st.markdown("<div class='custom-container'>", unsafe_allow_html=True)
    st.header("I nostri migliori momenti insieme")
    st.image("https://i.ibb.co/67spRrzZ/IMG-20260718-151122.jpg", use_column_width=True)
    st.image("https://i.ibb.co/zVJ7tzK5/IMG-20260718-151147.jpg", use_column_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCHERMATA 4: PROMESSA ---
with tab4:
    st.markdown("<div class='custom-container'>", unsafe_allow_html=True)
    st.header("Una promessa per il futuro")
    st.markdown("<h2 style='font-size: 40px; color: #d63384; margin-bottom: 20px;'>Giuro sulla tua vita</h2>", unsafe_allow_html=True)
    st.markdown("<div style='font-size: 100px; text-align: center;'>❤️ ∞</div>", unsafe_allow_html=True)
    st.markdown("<h3 style='font-style: italic; color: #555;'>Noi, per sempre</h3>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- SCHERMATA 5: AUGURI FINALI ---
with tab5:
    st.markdown("<div class='custom-container'>", unsafe_allow_html=True)
    st.header("Buon anniversario Ilenia!")
    st.image("https://i.ibb.co/Df9CBr17/IMG-20260718-151221.jpg", use_column_width=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.write("Sei la persona più importante della mia vita. Ti amo immensamente.")
    st.balloons()
    st.markdown("</div>", unsafe_allow_html=True)
