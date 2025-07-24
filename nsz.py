import streamlit as st
import random

# --- SENİN ÖZEL SEVGİ NEDENLERİN ---
# Buradaki listeye, sevgilini neden sevdiğini anlatan cümleleri ekleyebilirsin.
# Her bir nedeni tırnak içine al ve aralarına virgül koymayı unutma.
# Ne kadar çok eklersen, o kadar farklı seçenek çıkar!
sevgi_nedenleri = [
    "Gülüşünü seviyorum, bana dünyaları veriyor.",
    "Yanımda olman, bana her zaman güç veriyor.",
    "Zekana hayranım, her konuştuğumuzda yeni şeyler öğreniyorum.",
    "En sevdiğim rengin senin gözlerinin rengi olması.",
    "Bana her zaman destek olmanı ve beni motive etmeni seviyorum.",
    "Küçük sürprizlerin ve düşünceli hallerin beni mutlu ediyor.",
    "Seninle geçirdiğim her anın değerli olması.",
    "Bana hissettirdiğin güven duygusu.",
    "Birlikte saçmalamayı ve kahkahalar atmayı seviyorum.",
    "Hayallerime inanmanı ve beni desteklemeni seviyorum.",
    "Sabah uyandığımda aklıma ilk gelen kişi olman.",
    "Her zaman beni dinlemen ve anlamaya çalışman.",
    "En zor zamanlarımda bile yanımda olman.",
    "Seninle olmak, en sevdiğim yer olmak demek.",
    "Hayatıma kattığın pozitif enerji ve neşe.",
    "Bana hissettirdiğin eşsiz aşk duygusu.",
    "Her detayı düşünerek beni şaşırtman.",
    "Sesini duymak, günümü güzelleştiriyor.",
    "Yanında kendim olabildiğim tek yer.",
    "Birlikte sessizliğin bile anlamlı olması.",
    "En kötü günümde bile beni güldürebilmen.",
    "Sana her baktığımda kalbimin hızlı atması.",
    "Birlikte kahve içmek bile seninle güzel.",
    "Hayatıma anlam katmanı seviyorum.",
    "Bana kendimi özel hissettirmen.",
    "Her zorluğa seninle göğüs gerebileceğimi bilmem.",
    "Senden her gün yeni bir şey öğreniyorum."
    # Buraya kendi özel nedenlerini ekle!
    # Örnek: "En sevdiğim yemeği mükemmel yapmanı seviyorum.",
    # Örnek: "Birlikte izlediğimiz o filmi hatırlamanı seviyorum.",
    # Örnek: "Beni sabırla dinlemeni seviyorum.",
]

# --- STREAMLIT UYGULAMASI ---

# Sayfa ayarları
st.set_page_config(layout="centered", page_title="Senin İçin Bir Neden", page_icon="❤️")

st.title("Sevgilim, Seni Neden Mi Seviyorum? İşte Bir Neden:")
st.markdown("---")

# Oturum durumu (Hafıza) - Hangi nedenin gösterildiğini takip etmek için
if 'current_reason_index' not in st.session_state:
    st.session_state.current_reason_index = None # Henüz bir neden gösterilmedi

# Butona basıldığında çalışacak fonksiyon
def get_random_reason():
    # Rastgele bir neden seç ve oturum hafızasına kaydet
    st.session_state.current_reason_index = random.choice(range(len(sevgi_nedenleri)))

# Buton
st.button("Yeni Bir Neden Keşfet ❤️", on_click=get_random_reason, use_container_width=True)

st.markdown("---")

# Nedeni gösterme alanı
if st.session_state.current_reason_index is not None:
    st.markdown(f"## {sevgi_nedenleri[st.session_state.current_reason_index]}")
    st.markdown("---")
    st.markdown("Umarım bu küçük jest sana sevgimi bir kez daha hatırlatır. Seni seviyorum! 🥰")
else:
    st.info("Yukarıdaki butona basarak sana olan sevgimin nedenlerinden birini keşfedebilirsin!")

# Uygulamanın en altına küçük bir not
st.markdown("---")
st.caption("Bu uygulama, sana özel olarak kodlandı. 💖")