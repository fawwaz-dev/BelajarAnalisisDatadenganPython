import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# Load dataset
def load_data():
    df = pd.read_csv("dashboard/main_data.csv", parse_dates=["date"])
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Data")
start_date = st.sidebar.date_input("Start Date", df["date"].min())
end_date = st.sidebar.date_input("End Date", df["date"].max())
selected_pollutant = st.sidebar.radio("Select Pollutant", ["PM2.5", "PM10"])

# Ensure data type compatibility
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filter dataset
filtered_df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

st.title("Air Pollution Dashboard")
st.write("### Hubungan antara tingkat polusi udara dan suhu")

# Check if 'TEMP' column exists
if "TEMP" in filtered_df.columns:
    if not filtered_df.empty:
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.scatterplot(data=filtered_df, x="TEMP", y=selected_pollutant, ax=ax)
        ax.set_title(f"Hubungan {selected_pollutant} dan Suhu")
        st.pyplot(fig)
    else:
        st.warning("Tidak ada data untuk rentang tanggal yang dipilih.")
else:
    st.error("Kolom 'TEMP' tidak ditemukan dalam dataset.")

# Korelasi antara PM2.5, PM10, dan Suhu
if "TEMP" in filtered_df.columns and not filtered_df.empty:
    correlation = filtered_df[["PM2.5", "PM10", "TEMP"]].corr()
    st.write("### Korelasi antara Polusi Udara dan Suhu")
    st.dataframe(correlation)
else:
    st.warning("Tidak ada data yang tersedia atau kolom 'TEMP' tidak ditemukan.")

st.write("### Pola Musiman dalam Tingkat Polusi Udara")
if not filtered_df.empty:
    filtered_df["date"] = pd.to_datetime(filtered_df["date"])
    filtered_df.set_index("date", inplace=True)
    monthly_data = filtered_df[selected_pollutant].resample('M').mean()
    
    decomposition = seasonal_decompose(monthly_data.dropna(), model='additive')
    
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(12, 10))
    decomposition.observed.plot(ax=ax1)
    ax1.set_ylabel('Observed')
    decomposition.trend.plot(ax=ax2)
    ax2.set_ylabel('Trend')
    decomposition.seasonal.plot(ax=ax3)
    ax3.set_ylabel('Seasonal')
    decomposition.resid.plot(ax=ax4)
    ax4.set_ylabel('Residual')
    st.pyplot(fig)
else:
    st.warning("Tidak ada data untuk rentang tanggal yang dipilih.")

st.write("Gunakan sidebar untuk mengatur rentang tanggal dan memilih jenis polutan.")
