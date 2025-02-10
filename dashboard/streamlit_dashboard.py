
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dashboard Kualitas Udara")
data = pd.read_csv("main_data.csv")

st.sidebar.header("Filter")
station = st.sidebar.selectbox("Pilih Stasiun", data["station"].unique())
filtered_data = data[data["station"] == station]

st.subheader("Visualisasi PM2.5")
fig, ax = plt.subplots()
sns.histplot(filtered_data["PM2.5"].dropna(), bins=30, kde=True, ax=ax)
st.pyplot(fig)
