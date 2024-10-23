import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Crawling Media", layout="wide")
with open('assets/css/dashboard.css')as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
# Create main content area
st.sidebar.image("assets/img/logo2.png", width=168) 
st.title("Crawling Media")

# Create search bar
search_text = st.text_input("Search", "")

# Load data
data = pd.DataFrame({
    "No": [1, 2, 3, 4],
    "Judul": ["Heboh Mobil Listrik Terbakar di Korea, Hyundai Pastikan Baterainya Aman"] * 4,
    "Tanggal": ["Selasa, 1 Januari 2024 12:12"] * 4,
    "Link": ["https://oto.detik.com/mobil-listrik/d-7571297/heboh-mobil-listrik-terbakar-di-korea-hyundai-pastikan-baterainya-aman"] * 4,
    "Penulis": ["Dina Rayanti"] * 4,
    "News Value": [52250000, 30000000, 22500000, 22500000],
    "Detail": [
        "Di Korea Selatan heboh mobil listrik Mercedes-Benz EQE tiba-tiba terbakar dan merembet ke 140 mobil lainnya di parkiran basement. Insiden ini menambah kekhawatiran orang untuk beralih menggunakan mobil listrik.\n\nPara ahli berspekulasi, mobil listrik tersebut mungkin terlibat dalam tabrakan sebelum kejadian, yang dapat merusak baterai dan menyebabkan panas berlebih. Dalam kejadian itu, tidak disebutkan merek bateral yang digunakan."
    ] * 4,
    "Ringkasan": [
        "Di Korea Selatan heboh mobil listrik Mercedes-Benz EQE tiba-tiba terbakar dan merembet ke 140 mobil lainnya di parkiran basement."
    ] * 4,
    "Media": ["DetikOto"] * 4,
    "Deskripsi": ["Mobil listrik Mercedes-Benz EQE terbakar di Korea Selatan."] * 4,
})

# Filter data based on search text
filtered_data = data[data["Judul"].str.contains(search_text, case=False)]

# Create table
st.write(filtered_data)