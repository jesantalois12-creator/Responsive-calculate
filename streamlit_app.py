import streamlit as st

# Mengatur konfigurasi halaman agar responsif
st.set_page_config(page_title="Kalkulator Pipa", page_icon="🧮", layout="centered")

# --- JUDUL APLIKASI ---
st.title("Responsive Calculate")
st.markdown("---")

# --- FITUR PILIHAN UKURAN PIPA ---
pilihan_pipa = st.selectbox(
    "Silakan Pilih Ukuran Pipa:",
    ["4\"", "5\"", "6\"", "7\"", "8\"", "9\"", "10\"", "12\"", "14\"", "16\"", "18\"", "20\"", "22\"", "24\""],
    index=4 # Default otomatis memilih pipa 8"
)

st.markdown("---")

# --- LOGIKA DATA OTOMATIS BERDASARKAN PILIHAN (8 TITIK) ---
if pilihan_pipa == "4\"":
    od, circum, miter = "114,3 mm", "359,1 mm", "15°"
    t45, t90, t135, t180 = "4,5 mm", "15,2 mm", "26,0 mm", "30,5 mm"
elif pilihan_pipa == "5\"":
    od, circum, miter = "141,3 mm", "443,9 mm", "15°"
    t45, t90, t135, t180 = "5,5 mm", "18,9 mm", "32,3 mm", "37,8 mm"
elif pilihan_pipa == "6\"":
    od, circum, miter = "168,3 mm", "528,7 mm", "15°"
    t45, t90, t135, t180 = "6,6 mm", "22,5 mm", "38,5 mm", "45,1 mm"
elif pilihan_pipa == "8\"":
    od, circum, miter = "219,1 mm", "688,3 mm", "15°"
    t45, t90, t135, t180 = "8,6 mm", "29,3 mm", "50,1 mm", "58,7 mm"
elif pilihan_pipa == "10\"":
    od, circum, miter = "273,0 mm", "857,7 mm", "15°"
    t45, t90, t135, t180 = "10,7 mm", "36,5 mm", "62,4 mm", "73,1 mm"
else:
    # Perkiraan otomatis untuk ukuran pipa lainnya menggunakan perkalian skala
    nilai_inci = float(pilihan_pipa.replace('"', ''))
    od = f"{round(nilai_inci * 27.4, 1)} mm"
    circum = f"{round(nilai_inci * 27.4 * 3.1415, 1)} mm"
    miter = "15°"
    t45 = f"{round(nilai_inci * 1.07, 1)} mm"
    t90 = f"{round(nilai_inci * 3.66, 1)} mm"
    t135 = f"{round(nilai_inci * 6.26, 1)} mm"
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

# --- BAGIAN 2: GARIS PANDUAN PEMOTONGAN (8 TITIK) ---
st.subheader("📝 Garis Panduan Pemotongan untuk Welder (Tinggal Garis di Lapangan)")

st.write(
    "Untuk memotong pipa besi, pekerja cukup melingkari pipa dengan sabuk kertas, "
    "menandai **8 titik koordinat utama**, lalu membuat garis melengkung menghubungkan angka instan dari AI ini:"
)

# Menampilkan 8 koordinat lingkaran secara berurutan berputar
st.markdown(f"""
* **Titik 0° (Atas / Awal):** 0 mm
* **Titik 45° (Samping Kanan Atas):** {t45}
* **Titik 90° (Samping Kanan):** {t90}
* **Titik 135° (Samping Kanan Bawah):** {t135}
* **Titik 180° (Bawah / Puncak Lengkungan):** {t180}
* **Titik 225° (Samping Kiri Bawah):** {t135}
* **Titik 270° (Samping Kiri):** {t90}
* **Titik 315° (Samping Kiri Atas):** {t45}
""")
