import streamlit as str

# Mengatur konfigurasi halaman agar responsif
str.set_page_config(page_title="Kalkulator Pipa", page_icon="🧮", layout="centered")

# --- JUDUL APLIKASI ---
str.title("Responsive Calculate")

str.markdown("---")

# --- BAGIAN 1: RINGKASAN DATA TEKNIS ---
str.subheader("📋 Ringkasan Data Teknis Lapangan (Pipa 8 Inci - Schedule 40)")

# Menampilkan poin-poin data teknis
str.markdown("""
* **Diameter Luar Pipa (OD):** 219,1 mm
* **Keliling Pipa (Circumference):** 688,3 mm
* **Jumlah Segmen Potongan:** 4 segmen (*Lobster Back*)
* **Sudut Pemotongan Las (*Miter Angle*):** 15° per potongan segmen
""")

str.markdown("---")

# --- BAGIAN 2: GARIS PANDUAN PEMOTONGAN ---
str.subheader("📝 Garis Panduan Pemotongan untuk Welder (Tinggal Garis di Lapangan)")

# Deskripsi instruksi lapangan
str.write(
    "Untuk memotong pipa besi, pekerja cukup melingkari pipa dengan sabuk kertas, "
    "menandai 4 titik koordinat utama, lalu membuat garis melengkung mengikuti angka instan dari AI ini:"
)

# Menampilkan titik koordinat potongan pipa
str.markdown("""
* **Titik 0° (Atas):** 0 mm (Titik awal)
* **Titik 90° (Samping Kanan):** 29,3 mm
* **Titik 180° (Bawah / Puncak Lengkungan):** 58,7 mm
* **Titik 270° (Samping Kiri):** 29,3 mm
""")
