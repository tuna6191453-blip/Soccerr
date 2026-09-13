import streamlit as st
import pandas as pd
from mock_engine import generate_live_matches
from analyzer import analyze_matches
from config import SIGNAL_GREEN, SIGNAL_RED, SIGNAL_YELLOW

st.set_page_config(page_title="Smart Money & Value Bet Radar", layout="wide")

# CSS Yükleme
with open("assets/page_flip.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("⚽ Smart Money & Money Flow Radar")

# Sayfa Değiştirici (Defter / Kitap Çevirme Mantığı)
tab1, tab2 = st.tabs(["📖 Ana Ekran: Canlı Radar", "📚 Sayfa 2: Backtest & İstatistik"])

# Data Hazırlama
raw_data = generate_live_matches(12)
analyzed_data = analyze_matches(raw_data)

# TAB 1: CANLI RADAR
with tab1:
    st.subheader("Anlık Para Akışı Ve Sinyal Kartları")
    
    col_a, col_b, col_c = st.columns(3)
    green_count = len(analyzed_data[analyzed_data["signal_type"] == SIGNAL_GREEN])
    red_count = len(analyzed_data[analyzed_data["signal_type"] == SIGNAL_RED])
    yellow_count = len(analyzed_data[analyzed_data["signal_type"] == SIGNAL_YELLOW])
    
    col_a.metric("🟩 Akıllı Para Sinyali", f"{green_count} Maç")
    col_b.metric("🟥 Tuzak/Gizli Hacim", f"{red_count} Maç")
    col_c.metric("🟨 Sakatlık/Haber Uyarısı", f"{yellow_count} Maç")
    
    st.divider()
    
    for _, row in analyzed_data.iterrows():
        sig = row["signal_type"]
        card_class = "card-green" if sig == SIGNAL_GREEN else ("card-red" if sig == SIGNAL_RED else "card-yellow")
        
        st.markdown(f"""
        <div class="{card_class}">
            <h4>{row['home_team']} vs {row['away_team']} <small>({row['match_time']})</small></h4>
            <p><b>Açılış Oran:</b> {row['open_odds']} ➡️ <b>Anlık Oran:</b> {row['current_odds']} (<b>Düşüş: %{round(row['odds_drop_pct']*100,1)}</b>)</p>
            <p><b>Borsa Toplam Hacim:</b> €{row['total_volume']:,} | <b>Ev Sahibi Hacim Payı: %{round(row['home_volume_pct']*100,1)}</b></p>
            <p><b>Sinyal Skoru:</b> {round(row['signal_score'],2)}</p>
        </div>
        """, unsafe_allow_html=True)

# TAB 2: BACKTEST & İSTATİSTİK
with tab2:
    st.subheader("Geçmiş Performans & Doğruluk Testi")
    st.write("Son 500 Maç Üzerindeki Sinyal Başarı Oranları (Simüle Edilmiş Tarihsel Veri)")
    
    mock_history = pd.DataFrame({
        "Sinyal Tipi": ["Akıllı Para (Yeşil)", "Tuzak Risk (Kırmızı)", "Haber/Sakatlık (Sarı)"],
        "Toplam Maç": [142, 89, 115],
        "Kazanma Oranı (%)": [76.8, 38.2, 54.1],
        "Ortalama ROI (%)": [+18.4, -12.1, +3.5]
    })
    
    st.dataframe(mock_history, use_container_width=True)
    st.bar_chart(mock_history.set_index("Sinyal Tipi")["Kazanma Oranı (%)"])
