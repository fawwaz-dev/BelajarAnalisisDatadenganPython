import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Pastikan file berada di lokasi yang benar
file_path = os.path.join(os.path.dirname(__file__), "main_data.csv")

# Coba membaca file dengan pengecekan error
try:
    data = pd.read_csv(file_path)
except FileNotFoundError:
    st.error(f"File 'main_data.csv' tidak ditemukan di {file_path}. Pastikan file tersedia di direktori yang benar.")
    st.stop()

st.title("Dashboard Kualitas Udara")

# Sidebar filter
st.sidebar.header("Filter")
station = st.sidebar.selectbox("Pilih Stasiun", data["station"].unique())

# Filter data berdasarkan stasiun yang dipilih
filtered_data = data[data["station"] == station]

# Visualisasi PM2.5
st.subheader("Visualisasi PM2.5")
fig, ax = plt.subplots()
sns.histplot(filtered_data["PM2.5"].dropna(), bins=30, kde=True, ax=ax)
st.pyplot(fig)
