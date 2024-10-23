import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Crawling Media",
    layout="wide",
    initial_sidebar_state="expanded",
)
with open('assets/css/dashboard.css')as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
st.sidebar.image("assets/img/logo2.png", width=168) 
st.title("Crawling Media")

# st.markdown("<hr style='border-color: #ccc; border-width: 2px;'>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Start Date", value=datetime.today().date())

with col2:
    end_date = st.date_input("End Date", value=datetime.today().date())

selected_media = st.multiselect("Media Berita", ["Antaranews", "DetikOto"], ["Antaranews"])
selected_keyword = st.multiselect("Keyword", ["Hyundai", "Hyundai Gowa"], ["Hyundai"])
st.button("Submit", key="submit")