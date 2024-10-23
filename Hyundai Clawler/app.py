import streamlit as st
st.set_page_config(page_title="My Multipage App", layout="wide")

# load css
with open('assets/css/login.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

st.sidebar.image("assets/img/logo.png", width=168)
st.sidebar.image("assets/img/logo-text.png", width=437)

st.header("Login")
email = st.text_input("Email Address")
password = st.text_input("Password", type="password")
if st.button("Sign In"):
    # Authentication logic goes here
    st.success("Logged in successfully!")
    
    #redirect to dashboard
    st.switch_page("pages/dashboard.py")

st.caption("Forgot Password?")


