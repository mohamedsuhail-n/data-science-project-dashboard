import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Connect to the SQLite DB
conn = sqlite3.connect('sales_data.db')
query = "SELECT * FROM sales"
df = pd.read_sql(query, conn)

# Title
st.title("📊 Sales Data Dashboard")

# Filters
year = st.selectbox("Select Year", sorted(df['year'].unique()))
filtered_df = df[df['year'] == year]

# KPIs
total_rent = filtered_df['total_rent'].sum()
user_count = filtered_df['user_count'].sum()
avg_temp = filtered_df['avg_temp'].mean()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Rent", f"{total_rent:,.0f}")
col2.metric("👥 User Count", f"{user_count:,.0f}")
col3.metric("🌡️ Avg Temp", f"{avg_temp:.2f} °C")

# Monthly Revenue Chart
monthly = filtered_df.groupby('month')['total_rent'].sum().reset_index()

fig, ax = plt.subplots()
ax.plot(monthly['month'], monthly['total_rent'], marker='o')
ax.set_xlabel("Month")
ax.set_ylabel("Total Rent")
ax.set_title("Monthly Rent Trend")
st.pyplot(fig)

# Optional: Show data table
if st.checkbox("Show Raw Data"):
    st.dataframe(filtered_df)
