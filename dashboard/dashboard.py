import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 📌 Load dataset dari dalam folder dashboard
data = pd.read_csv("dashboard/main_data.csv")  

# Buat kolom datetime
data["date"] = pd.to_datetime(data[["year", "month", "day", "hour"]])

# 📌 Sidebar filter
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Tanggal Mulai", pd.to_datetime("2013-01-01"))
end_date = st.sidebar.date_input("Tanggal Akhir", pd.to_datetime("2017-12-31"))
selected_station = st.sidebar.selectbox("Pilih Stasiun", data["station"].unique())

# 📌 Filter data berdasarkan input pengguna
filtered_data = data[
    (data["date"] >= pd.Timestamp(start_date)) &
    (data["date"] <= pd.Timestamp(end_date)) &
    (data["station"] == selected_station)
]

# 📌 Visualisasi PM2.5 dan PM10
st.header("Hubungan antara PM2.5 dan PM10")
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x="PM2.5", y="PM10", hue="TEMP", data=filtered_data, ax=ax)
st.pyplot(fig)
