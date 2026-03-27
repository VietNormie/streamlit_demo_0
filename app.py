# app.py
import streamlit as st

st.set_page_config(page_title="Demo Streamlit", page_icon="🚀")

st.title("Demo Streamlit trên Community Cloud")
st.write("Đây là app demo siêu đơn giản.")

name = st.text_input("Tên của bạn")
age = st.slider("Tuổi", 1, 100, 25)

if st.button("Chào tôi"):
    st.success(f"Xin chào {name or 'bạn'}! Bạn {age} tuổi.")
