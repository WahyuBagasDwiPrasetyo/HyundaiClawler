import streamlit as st

st.set_page_config(
    page_title="User Add",
    layout="wide",
    initial_sidebar_state="expanded",
)
with open('assets/css/dashboard.css')as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
st.sidebar.image("assets/img/logo2.png", width=168) 
st.title("User Add Form")

st.header("Please fill in the details below:")

nama_depan = st.text_input("Nama Depan")
nama_belakang = st.text_input("Nama Belakang")
email = st.text_input("Email")
nomor_telepon = st.text_input("Nomor Telepon")
username = st.text_input("Username")
tanggal_lahir = st.date_input("Tanggal Lahir")

if st.button("Submit"):
    st.success(f"User {username} added successfully!")