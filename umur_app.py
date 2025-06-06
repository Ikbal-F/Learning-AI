import streamlit as st
from datetime import datetime

st.title("📅 Tebak Umur")
tanggal_lahir = st.date_input("Masukkan tanggal lahir kamu:",
                              format= "DD/MM/YYYY",
                              min_value=datetime(1990,1,1).date(),
                              max_value=datetime.today().date())

usia = datetime.today().date()-tanggal_lahir
usia_tahun = usia.days // 365

if st.button("Hitung Umur"):
    st.write(f"Umur kamu adalah {usia_tahun} tahun")