import streamlit as st

st.title("🌤️ Prediksi Mood Berdasarkan Cuaca")
st.write("Cuaca menentukan mood Kamu...😘")
cuaca = st.selectbox("Bagaimana cuaca hari ini?", ["cerah", "berawan", "panas", "dingin", "berangin", "hujan"])
if cuaca == "cerah":
    mood = "Kayaknya Kamu akan senang hari ini"
elif cuaca == "berawan":
    mood = "Kamu akan kurang bersemangat hari ini, ngopi dulu yuk!"
elif cuaca == "panas":
    mood = "Awas, kendalikan amarah kamu. Cuaca panas suka bikin emosi"
elif cuaca == "dingin":
    mood = "Kamu akan pengen minum minuman hangat terus deh"
elif cuaca == "berangin":
    mood = "Kamu akan lemes dan lesu karena masuk angin 😢"
else:
    mood = "Bawaannya melow terus dehh..😫"

if st.button("Prediksi"):
    st.write(f"{mood}")


