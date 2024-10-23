import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(page_title="Dashboard", layout="wide")
with open('assets/css/dashboard.css')as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

st.sidebar.image("assets/img/logo2.png", width=168) 

# def show():

# Creating left and right columns
col1, col2 = st.columns(2)

# Placeholder for the left column
with col1:
    metric1, metric2 = st.columns(2)
    # Top metrics
    news_value, article_count = 14744, 14744
    with metric1:
        st.metric("News Value", news_value, "+13.6%", delta_color="normal")
    with metric2:
        st.metric("Jumlah Pemberitaan", article_count, "-13.6%", delta_color="normal")

    # Top Media Ranking
    st.subheader("Top Media Ranking")
    media = ["Kompas", "Detik.com", "Oto Driver", "CNN", "IDN Times", "Liputan6", "Kumparan", "Pikiran Rakyat", "Tempo.co", "Antara News"]
    article_counts = [90, 85, 80, 75, 70, 65, 60, 55, 50, 45]
    fig, ax = plt.subplots()
    ax.barh(media, article_counts)
    ax.set_xlabel("Jumlah Berita")
    st.pyplot(fig)

# Dashboard content for the right column
with col2:
    # Trend Pemberitaan
    st.subheader("Tren Pemberitaan")
    dates = [1, 7, 14, 21, 28]
    article_counts = [400, 500, 800, 500, 1000]
    fig, ax = plt.subplots(figsize=(12,6))
    ax.plot(dates, article_counts)
    ax.set_xticks(dates)
    ax.set_yticks(np.arange(0, 2000, 250))
    st.pyplot(fig)

    # Top Penulis Ranking
    st.subheader("Top Penulis Ranking")
    names = ["Dina Rayanti", "Septian ", "Rizal", "Dwi", "Rudi", "Rahmat", "Rudi", "Rudi", "Rudi", "Rudi"]
    article_counts = [90, 85, 80, 75, 70, 65, 60, 55, 50, 45]

    # Create a pie chart
    fig, ax = plt.subplots(figsize=(10,5))
    ax.pie(article_counts, labels=names, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
    st.pyplot(fig)

