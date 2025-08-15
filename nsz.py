import streamlit as st
from PIL import Image

# Sayfa yapılandırmasını ayarlar
st.set_page_config(
    page_title="Mxrtt",
    page_icon="🟥",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---
# Sayfanın koyu temalı ve özel stilini ayarlar
# ---
st.markdown(
    """
    <style>
    /* Ana arka plan rengini siyah yapar */
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    /* Metin rengini kırmızı yapar ve gölge ekler */
    h1 {
        color: #FF0000 !important;
        text-shadow: 0 0 10px #ff0000;
        font-weight: bold;
        text-align: center;
        font-size: 3rem;
    }
    p {
        color: #FF0000 !important;
        text-align: center;
        font-size: 1.25rem;
    }
    /* Yatay çizginin rengi */
    hr {
        border-top: 1px solid #4a5568;
    }
    /* St.markdown ile gelen p etiketini hedeflemek için */
    .stMarkdown p {
        color: #FF0000 !important;
        text-align: center;
        font-size: 1.25rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---
# Sayfa İçeriği
# ---

# Mxrtt başlığı
st.title('Mxrtt')

# Tanıtım metni
st.markdown(
    'I don\'t know what to write here, I was just experimenting and writing code, by the way, my closest friend Ömxr is a complete idiot :D'
)

# Yatay çizgi
st.markdown("---")

# İkonları yan yana göstermek için sütunlar oluştur
col1, col2 = st.columns(2)

with col1:
    try:
        # discord_icon.png dosyasını 'icons' klasöründen yüklemeyi dener
        discord_icon = Image.open("icons/discord_icon.png")
        st.image(discord_icon, use_column_width=True)
    except FileNotFoundError:
        st.error("Discord ikonu bulunamadı! Lütfen dosyayı 'icons' klasörüne ekleyin.")

with col2:
    try:
        # spotify_icon.png dosyasını 'icons' klasöründen yüklemeyi dener
        spotify_icon = Image.open("icons/spotify_icon.png")
        st.image(spotify_icon, use_column_width=True)
    except FileNotFoundError:
        st.error("Spotify ikonu bulunamadı! Lütfen dosyayı 'icons' klasörüne ekleyin.")

