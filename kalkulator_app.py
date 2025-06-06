import streamlit as st

st.title("🛒 Kalkulator Diskon Belanja")
st.write("Selamat Berbelanja  di Toko Kami!")
total_belanja = st.number_input("Masukkan total belanja (Rp):", min_value=0,)

if total_belanja < 100_000:
    diskon = 0
elif total_belanja < 200_000:
    diskon = 0.05
elif total_belanja < 300_000:
    diskon = 0.08
else:
    diskon = 0.10

potongan = total_belanja * diskon
total_harga = total_belanja-potongan

if st.button("Hitung Diskon!"):
    st.write(f"Besar diskon: {int(diskon*100)}%")
    st.write(f"Jumlah potongan harga: Rp{potongan:,.0f}")
    st.write(f"Total harga setelah diskon: Rp{total_harga:,.0f}")


