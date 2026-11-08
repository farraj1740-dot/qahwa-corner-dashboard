from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Qahwa Corner Dashboard",
    page_icon="☕",
    layout="wide"
)

st.title("☕ Qahwa Corner Sales Dashboard")
st.caption("Sales data: January–June 2026")

@st.cache_data
def load_data():
    file_path = Path(__file__).parent / "cafe_sales.csv"
    return pd.read_csv(file_path)

df = load_data()

selected_branch = st.selectbox(
    "Select a branch",
    sorted(df["branch"].unique())
)

branch_data = df[df["branch"] == selected_branch]

total_revenue = branch_data["total_sar"].sum()
st.metric("Total Revenue", f"SAR {total_revenue:,.0f}")

product_revenue = (
    branch_data.groupby("product")["total_sar"]
    .sum()
    .sort_values(ascending=False)
)

st.subheader("Revenue by Product")
st.caption("Revenue in Saudi Riyals (SAR)")
st.bar_chart(product_revenue)
