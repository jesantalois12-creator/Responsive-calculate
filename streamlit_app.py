import streamlit as st

# Mengatur konfigurasi halaman agar responsif
st.set_page_config(page_title="Kalkulator Pipa", page_icon="🧮", layout="centered")

# --- JUDUL APLIKASI ---
st.title("Responsive Calculate")
st.markdown("---")

# --- FITUR PILIHAN UKURAN PIPA ---
# Membuat dropdown pilihan pipa dari 4 inci sampai 24 inci
pilihan_pipa = st.selectbox(
    "Silakan Pilih Ukuran Pipa:",
    ["4\"", "5\"", "6\"", "7\"", "8\"", "9\"", "10\"", "12\"", "14\"", "16\"", "18\"", "20\"", "22\"", "24\""],
    index=4 # Default otomatis memilih pipa 8" agar sama seperti gambar sebelumnya
)

st.markdown("---")

# --- LOGIKA DATA OTOMATIS BERDASARKAN PILIHAN ---
# Data tiruan sebagai contoh responsif, angka akan berubah otomatis saat Anda memilih pipa di web
if pilihan_pipa == "4\"":
    od, circum, miter, t90, t180 = "114,3 mm", "359,1 mm", "15°", "15,2 mm", "30,5 mm"
elif pilihan_pipa == "5\"":
    od, circum, miter, t90, t180 = "141,3 mm", "443,9 mm", "15°", "18,9 mm", "37,8 mm"
elif pilihan_pipa == "6\"":
    od, circum, miter, t90, t180 = "168,3 mm", "528,7 mm", "15°", "22,5 mm", "45,1 mm"
elif pilihan_pipa == "8\"":
    od, circum, miter, t90, t180 = "219,1 mm", "688,3 mm", "15°", "29,3 mm", "58,7 mm"
elif pilihan_pipa == "10\"":
    od, circum, miter, t90, t180 = "273,0 mm", "857,7 mm", "15°", "36,5 mm", "73,1 mm"
else:
    # Angka perkiraan otomatis untuk ukuran pipa lainnya (7", 9", dan 12" sampai 24")
    nilai_inci = float(pilihan_pipa.replace('"', ''))
    od = f"{round(nilai_inci * 27.4, 1)} mm"
    circum = f"{round(nilai_inci * 27.4 * 3.1415, 1)} mm"
    miter = "15°"
    t90 = f"{round(nilai_inci * 3.66, 1)} mm"
    t180 = f"{round(nilai_inci * 3.66 * 2, 1)} mm"

# --- BAGIAN 1: RINGKASAN DATA TEKNIS ---
st.subheader(f"📋 Ringkasan Data Teknis Lapangan (Pipa {pilihan_pipa} - Schedule 40)")

st.markdown(f"""
* **Diameter Luar Pipa (OD):** {od}
* **Keliling Pipa (Circumference):** {circum}
* **Jumlah Segmen Potongan:** 4 segmen (*Lobster Back*)
* **Sudut Pemotongan Las (*Miter Angle*):** {miter} per potongan segmen
""")

st.markdown("---")

# --- BAGIAN 2: GARIS PANDUAN PEMOTONGAN ---
st.subheader("📝 Garis Panduan Pemotongan untuk Welder (Tinggal Garis di Lapangan)")

st.write(
    "Untuk memotong pipa besi, pekerja cukup melingkari pipa dengan sabuk kertas, "
    "menandai 4 titik koordinat utama, lalu membuat garis melengkung mengikuti angka instan dari AI ini:"
)

st.markdown(f"""
* **Titik 0° (Atas):** 0 mm (Titik awal)
* **Titik 90° (Samping Kanan):** {t90}
* **Titik 180° (Bawah / Puncak Lengkungan):** {t180}
* **Titik 270° (Samping Kiri):** {t90}
""")
