import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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
    t45, t90, t135, t180 = 4.5, 15.2, 26.0, 30.5
elif pilihan_pipa == "5\"":
    od, circum, miter = "141,3 mm", "443,9 mm", "15°"
    t45, t90, t135, t180 = 5.5, 18.9, 32.3, 37.8
elif pilihan_pipa == "6\"":
    od, circum, miter = "168,3 mm", "528,7 mm", "15°"
    t45, t90, t135, t180 = 6.6, 22.5, 38.5, 45.1
elif pilihan_pipa == "8\"":
    od, circum, miter = "219,1 mm", "688,3 mm", "15°"
    t45, t90, t135, t180 = 8.6, 29.3, 50.1, 58.7
elif pilihan_pipa == "10\"":
    od, circum, miter = "273,0 mm", "857,7 mm", "15°"
    t45, t90, t135, t180 = 10.7, 36.5, 62.4, 73.1
else:
    # Perkiraan otomatis untuk ukuran pipa lainnya menggunakan perkalian skala
    nilai_inci = float(pilihan_pipa.replace('"', ''))
    od = f"{round(nilai_inci * 27.4, 1)} mm"
    circum = f"{round(nilai_inci * 27.4 * 3.1415, 1)} mm"
    miter = "15°"
    t45 = round(nilai_inci * 1.07, 1)
    t90 = round(nilai_inci * 3.66, 1)
    t135 = round(nilai_inci * 6.26, 1)
    t180 = round(nilai_inci * 3.66 * 2, 1)

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
* **Titik 0° (Atas / Awal):** 0.0 mm
* **Titik 45° (Samping Kanan Atas):** {t45} mm
* **Titik 90° (Samping Kanan):** {t90} mm
* **Titik 135° (Samping Kanan Bawah):** {t135} mm
* **Titik 180° (Bawah / Puncak Lengkungan):** {t180} mm
* **Titik 225° (Samping Kiri Bawah):** {t135} mm
* **Titik 270° (Samping Kiri):** {t90} mm
* **Titik 315° (Samping Kiri Atas):** {t45} mm
""")

st.markdown("---")

# --- BAGIAN 3: GRAFIK VISUALISASI DENGAN GARIS VERTIKAL HITAM ---
st.subheader("📊 Peta Grafik Lengkungan Potongan Pipa")

# Derajat untuk titik penandaan utama (0 sampai 360 derajat)
derajat_titik = np.array([0, 45, 90, 135, 180, 225, 270, 315, 360])
tinggi_titik = np.array([0.0, t45, t90, t135, t180, t135, t90, t45, 0.0])

# Membuat kurva halus gelombang miter menggunakan rumus matematika sinus
derajat_halus = np.linspace(0, 360, 200)
tinggi_halus = t180 * (1 - np.cos(np.radians(derajat_halus))) / 2

# Menggambar plot kurva menggunakan Matplotlib
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(derajat_halus, tinggi_halus, color="#1E88E5", linewidth=3, label="Garis Potong Welder")

# MENAMBAHKAN GARIS BANTU VERTIKAL WARNA HITAM PUTUS-PUTUS DARI BAWAH SAMPAI KE TITIK KURVA
for d, t in zip(derajat_titik, tinggi_titik):
    ax.vlines(x=d, ymin=0, ymax=t, color="#000000", linestyle="--", linewidth=1.2)

# Mengembalikan marker titik utama ke warna merah asli
ax.scatter(derajat_titik, tinggi_titik, color="#D32F2F", s=60, zorder=5, label="8 Titik Utama")

# Menambahkan teks petunjuk angka di setiap titik utama agar jelas di layar HP
for d, t in zip(derajat_titik[:-1], tinggi_titik[:-1]):
    ax.annotate(f"{t}mm", (d, t), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, fontweight='bold')

# Pengaturan desain grafis sumbu X dan Y
ax.set_title(f"Pola Mal Potong Sabuk Kertas - Pipa {pilihan_pipa}", fontsize=12, fontweight='bold')
ax.set_xlabel("Posisi Putaran Lingkaran Pipa (Derajat)", fontsize=10)
ax.set_ylabel("Tinggi Pemotongan (mm)", fontsize=10)
ax.set_xticks(derajat_titik)
ax.set_xlim(0, 360)
ax.set_ylim(-5, t180 + 15)
ax.grid(True, linestyle=":", alpha=0.3)
ax.legend(loc="upper right")

# Menampilkan grafik ke dalam halaman web Streamlit
st.pyplot(fig)
