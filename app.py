import streamlit as st
from datetime import datetime

# --- CONFIGURAZIONE ---
st.set_page_config(page_title="6 Mesi di Noi", page_icon="❤️", layout="centered")

# --- STILE CSS OTTIMIZZATO ---
st.markdown("""
    <style>
    /* Sfondo e font */
    .stApp { background-color: #fff5f6; }
    h1, h2, h3 { color: #d63384; font-family: 'Arial', sans-serif; text-align: center; }
    
    /* Box stile 'carta' */
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 25px;
        box-shadow: 0 4px 10px rgba(214, 51, 132, 0.2);
        margin: 10px 0;
        border: 2px solid #ffccd5;
    }
    
    /* Numeri del timer */
    .timer-text {
        font-size: 28px;
        font-weight: bold;
        color: #b02a5c;
        text-align: center;
    }
    
    /* Immagini centrate e adattive */
    img { border-radius: 15px; width: 100% !important; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

# --- CALCOLI ---
start = datetime(2026, 1, 18, 23, 12, 0)
now = datetime.now()
diff = now - start
mesi = (now.year - start.year) * 12 + (now.month - start.month)
if now.day < start.day: mesi -= 1

# --- INTERFACCIA ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["❤️", "⏳", "📸", "📜", "✨"])

with tab1:
    st.markdown("<div class='card'><h1>6 Mesi di Noi</h1><p style='text-align:center'>Emanuele ❤️ Mia</p></div>", unsafe_allow_html=True)

with tab2:
    st.header("Il nostro tempo")
    st.markdown(f"""
        <div class='card'><div class='timer-text'>📅 {mesi} Mesi</div></div>
        <div class='card'><div class='timer-text'>☀️ {diff.days} Giorni</div></div>
        <div class='card'><div class='timer-text'>⏱️ {int(diff.total_seconds()):,} Secondi</div></div>
    """, unsafe_allow_html=True)

with tab3:
    st.header("Momenti")
    st.image("https://i.ibb.co/67spRrzZ/IMG-20260718-151122.jpg")
    st.image("https://i.ibb.co/zVJ7tzK5/IMG-20260718-151147.jpg")

with tab4:
    st.markdown("<div class='card'><h2>Giuro sulla tua vita</h2><br><h1 style='font-size:60px'>❤️ ∞</h1></div>", unsafe_allow_html=True)

with tab5:
    st.header("Auguri Mia!")
    st.image("https://i.ibb.co/Df9CBr17/IMG-20260718-151221.jpg")
    st.balloons()
