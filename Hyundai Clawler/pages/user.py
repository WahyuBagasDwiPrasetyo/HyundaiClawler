import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Crawling Media", layout="wide")
with open('assets/css/dashboard.css')as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
# Create main content area
st.sidebar.image("assets/img/logo2.png", width=168) 
st.title("User")

# Create search bar
search_text = st.text_input("Search", "")

# Load data
data = pd.DataFrame({
    "No": [1, 2, 3, 4],
    "Nama Depan": ["Dina", "Rizky", "Rizal", "Dwi"],
    "Nama Belakang": ["Rayanti", "Handoko", "Febriansyah", "Kurniawan"],
    "Email": ["rayanti123@gmail.com", "handokoRizky@gmail.com", "rizal1232@gmail.com", "wawan@gmail.com"],
    "Nomor Telepon": ["08123456789", "08123456789", "08123456789", "08123456789"],
    "Username": ["dina123", "rizky123", "rizal123", "dwi123"],
    "Tanggal Lahir": ["1998-01-01", "1998-01-01", "1998-01-01", "1998-01-01"],
})

# Filter data based on search text
filtered_data = data[data["Nama Depan"].str.contains(search_text, case=False)]

# Create table
st.write(filtered_data)