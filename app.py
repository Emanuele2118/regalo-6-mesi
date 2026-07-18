import streamlit as st
import time
from datetime import datetime

# --- CONFIGURAZIONE PAGINA ---
st.set_page_config(page_title="6 Mesi di Noi", page_icon="❤️", layout="centered")

# --- STILE GRAFICO ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #fff5f8 0%, #ffffff 100%); }
    h1, h2, h3 { font-family: 'Georgia', serif; color: #5d275c; text-align: center; }
    .custom-container { background-color: rgba(255, 255, 255, 0.9); padding: 30px; border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 20px; }
    .timer-box { text-align: center; background-color: #fff0f5; padding: 20px; border-radius: 15px; border-left: 5px solid #d63384; margin-bottom: 15px; }
    .timer-value { font-size: 36px; color: #4a4a4a; font-weight: 900; }
    </style>
""", unsafe_allow_html=True)

start_date = datetime(2026, 1, 18, 23, 12, 0)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["❤️ Inizio", "⏳ Il Nostro Tempo", "📸 Momenti", "📜 Promessa", "✨ Auguri"])

with tab1:
    st.markdown("<div class='custom-container'><h1>6 Mesi di Noi</h1><p style='text-align:center;'>Emanuele ❤️ Mia</p></div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<div class='custom-container'>", unsafe_allow_html=True)
    st.header("Il nostro tempo insieme")
    now = datetime.now()
    diff = now - start_date
    mesi = (now.year - start_date.year) * 12 + (now.month - start_date.month)
    if now.day < start_date.day: mesi -= 1
    
    st.markdown(f"<div class='timer-box'><div class='timer-value'>{mesi} Mesi</div></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='timer-box'><div class='timer-value'>{diff.days} Giorni</div></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='timer-box'><div class='timer-value'>{int(diff.total_seconds()):,} Secondi</div></div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.markdown("<div class='custom-container'>", unsafe_allow_html=True)
    st.header("I nostri momenti")
    st.image("https://i.ibb.co/67spRrzZ/IMG-20260718-151122.jpg")
    st.image("https://i.ibb.co/zVJ7tzK5/IMG-20260718-151147.jpg")
    st.markdown("</div>", unsafe_allow_html=True)

with tab4:
    st.markdown("<div class='custom-container'>", unsafe_allow_html=True)
    st.header("Giuro sulla tua vita")
    st.markdown("<h2 style='font-size: 50px;'>❤️ ∞</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with tab5:
    st.markdown("<div class='custom-container'>", unsafe_allow_html=True)
    st.header("Auguri Mia!")
    st.image("https://i.ibb.co/Df9CBr17/IMG-20260718-151221.jpg")
    st.balloons()
    st.markdown("</div>", unsafe_allow_html=True)
