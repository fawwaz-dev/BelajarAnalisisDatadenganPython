# Air Quality Analysis

## Pendahuluan

Notebook ini bertujuan untuk menganalisis data kualitas udara menggunakan beberapa teknik analisis lanjutan seperti **RFM Analysis**, **Geospatial Analysis**, dan **Clustering**. Hasil analisis akan divisualisasikan dalam dashboard interaktif menggunakan **Streamlit**.

## Struktur Direktori

Pastikan struktur direktori proyek mengikuti format berikut sebelum melakukan submission:

```
submission
├───dashboard
|   ├───main_data.csv
|   └───dashboard.py
├───data
|   ├───data_1.csv
|   └───data_2.csv
├───notebook.ipynb
├───README.md
├───requirements.txt
└───url.txt
```

## Langkah-langkah Analisis Data

1. **Membaca dan Membersihkan Data**

   - Mengimpor dan menggabungkan file CSV dalam folder `data/`
   - Memisahkan kolom yang tidak terstruktur menjadi format tabular yang bersih
   - Menghapus nilai yang hilang atau tidak relevan

2. **Eksplorasi Data**
   - Statistik deskriptif pada variabel utama seperti **PM2.5, PM10, SO2, NO2, CO, O3**
   - Visualisasi distribusi menggunakan histogram dan boxplot
3. **RFM Analysis** (Recency, Frequency, Monetary)
   - Menghitung _Recency_: Jumlah hari sejak pengukuran terakhir di setiap stasiun
   - Menghitung _Frequency_: Jumlah total pengukuran dalam periode tertentu
   - Menghitung _Monetary_: Rata-rata tingkat polusi udara
4. **Geospatial Analysis**
   - Menggunakan **Folium** untuk memetakan tingkat polusi berdasarkan stasiun pemantauan
   - Analisis kepadatan polusi udara dalam wilayah tertentu
5. **Clustering Analysis** (tanpa Machine Learning)
   - Melakukan _manual grouping_ berdasarkan kategori polusi udara (baik, sedang, buruk)
   - Menggunakan teknik _binning_ untuk membagi data dalam interval tertentu
6. **Membuat Dashboard dengan Streamlit**
   - Dashboard interaktif untuk menampilkan hasil analisis
   - Menampilkan peta geospasial kualitas udara
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

```
pandas
numpy
matplotlib
seaborn
folium
streamlit
geopandas
```

### url.txt

Tambahkan tautan ke dashboard setelah deployment:

```
https://share.streamlit.io/username/project
```
