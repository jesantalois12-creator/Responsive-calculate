import streamlit as st
import pandas as pd

# Judul Utama Aplikasi dengan Emoji
st.title("🧮 Kalkulator & Grafik Interaktif")
st.write("Selamat datang! Silakan masukkan angka untuk menghitung dan melihat grafik simulasi.")

# --- BAGIAN 1: KALKULATOR INTERAKTIF ---
st.header("1. Kalkulator Sederhana")

# Kolom input angka bersebelahan
col1, col2 = st.columns(2)
with col1:
    angka1 = st.number_input("Masukkan Angka Pertama:", value=10)
with col2:
    angka2 = st.number_input("Masukkan Angka Kedua:", value=5)

# Pilihan operasi matematika menggunakan dropdown
operasi = st.selectbox("Pilih Operasi Matematika:", ["Penjumlahan (+)", "Pengurangan (-)", "Perkalian (x)", "Pembagian (/)"])

# Tombol untuk menghitung
if st.button("Hitung Sekarang!"):
    if operasi == "Penjumlahan (+)":
        hasil = angka1 + angka2
        st.success(f"Hasil dari {angka1} + {angka2} adalah: **{hasil}**")
    elif operasi == "Pengurangan (-)":
        hasil = angka1 - angka2
        st.success(f"Hasil dari {angka1} - {angka2} adalah: **{hasil}**")
    elif operasi == "Perkalian (x)":
        hasil = angka1 * angka2
        st.success(f"Hasil dari {angka1} x {angka2} adalah: **{hasil}**")
    elif operasi == "Pembagian (/)":
        if angka2 != 0:
            hasil = angka1 / angka2
            st.success(f"Hasil dari {angka1} / {angka2} adalah: **{hasil}**")
        else:
            st.error("Error: Angka kedua tidak boleh 0 untuk pembagian!")

# --- BAGIAN 2: GRAFIK DATA INTERAKTIF ---
st.write("---")
st.header("2. Simulasi Grafik Data")
st.write("Geser slider di bawah ini untuk melihat bagaimana grafik berubah secara langsung!")

# Slider interaktif untuk mengubah nilai data grafik
nilai_slider = st.slider("Atur Skala Pertumbuhan Data:", min_value=1, max_value=50, value=25)

# Membuat data acak berdasarkan input slider pengguna
data_grafik = pd.DataFrame({
    'Bulan': ['Januari', 'Februari', 'Maret', 'April', 'Mei'],
    'Pertumbuhan': [10 * nilai_slider, 20 * nilai_slider, 15 * nilai_slider, 35 * nilai_slider, 50 * nilai_slider]
})

# Menampilkan grafik garis interaktif
st.line_chart(data_grafik.set_index('Bulan'))
