# Air Quality Analysis

## Pendahuluan

Proyek ini bertujuan untuk menganalisis data kualitas udara dengan pendekatan analitis menggunakan Python. Hasil analisis akan divisualisasikan dalam dashboard interaktif menggunakan **Streamlit**.

## Struktur Direktori

Pastikan struktur direktori proyek mengikuti format berikut sebelum melakukan submission:

```
submission
├───dashboard
|   ├───main_data.csv
|   └───dashboard.py
├───data
|   ├───day.csv
|   ├───hour.csv
|   └───dan-lainnya.csv
├───notebook.ipynb
├───README.md
├───requirements.txt
└───url.txt (Jika menerapkan saran ketiga)
```

## Langkah-langkah Analisis Data

1. **Membaca dan Membersihkan Data**

   - Mengimpor dan menggabungkan file CSV dalam folder `data/`
   - Menghapus nilai yang hilang atau tidak relevan

2. **Eksplorasi Data**

   - Statistik deskriptif pada variabel utama seperti **PM2.5, PM10, SO2, NO2, CO, O3**
   - Visualisasi distribusi menggunakan histogram dan boxplot

3. **Pembuatan Dashboard dengan Streamlit**

   - Dashboard interaktif untuk menampilkan hasil analisis
   - Menampilkan visualisasi data dalam bentuk grafik
   - Menyediakan filter berdasarkan waktu dan lokasi

## Cara Menjalankan Dashboard

1. Pastikan semua library telah terinstall dengan menjalankan:
   ```sh
   pip install -r requirements.txt
   ```
2. Jalankan Streamlit dengan perintah:
   ```sh
   streamlit run dashboard/dashboard.py
   ```

## Berkas Tambahan

### requirements.txt

File ini berisi daftar pustaka yang digunakan dalam proyek ini.

### url.txt

Tambahkan tautan ke dashboard setelah deployment:

```
https://share.streamlit.io/username/project
```

Jika ada kendala atau saran, silakan beri masukan! 🚀
