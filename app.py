import streamlit as st

# Judul aplikasi
st.title("Aplikasi Quiz Sederhana")

# Teks biasa
st.write("Selamat datang di aplikasi quiz!")

# Input teks
name = st.text_input("Masukkan nama kamu:")

# Tombol
if st.button("Mulai Quiz"):
    st.write(f"Halo, {name}! Ayo kita mulai kuisnya.")

