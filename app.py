import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import plotly.express as px

st.set_page_config(page_title="Sales Analytics Dashboard", page_icon="📊", layout="wide")

@st.cache_data
def load_data():
    path = Path("python_data_analyst_sales_project_cleaned.csv")
    if not path.exists():
        st.error("python_data_analyst_sales_project_cleaned.csv is missing. Put it in the same folder as app.py.")
        st.stop()

    df = pd.read_csv(path)
    df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

    for col in ["Sales", "Profit", "Quantity", "Unit_Price"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["Sales"] = df["Sales"].fillna(df["Sales"].median())
    df["Profit"] = df["Profit"].fillna(df["Profit"].median())
    df["Quantity"] = df["Quantity"].fillna(1)

    df["Month_Year"] = df["Order_Date"].dt.to_period("M").astype(str)
    return df

def money(value):
    value = float(value)
    if abs(value) >= 10000000:
        return f"₹{value/10000000:.2f} Cr"
    if abs(value) >= 100000:
        return f"₹{value/100000:.2f} L"
    if abs(value) >= 1000:
        return f"₹{value/1000:.1f} K"
    return f"₹{value:,.0f}"

df = load_data()

st.markdown(
    "<h1 style='font-size:42px;'>📊 Sales Analytics Dashboard</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='font-size:17px;color:#6b7280;'>Python Data Analyst Portfolio Project • Pandas • NumPy • Streamlit • Plotly</p>",
    unsafe_allow_html=True
)

st.sidebar.header("📅 Date Filter")

min_date = df["Order_Date"].min().date()
max_date = df["Order_Date"].max().date()

date_range = st.sidebar.date_input(
    "Select date range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
    format="DD/MM/YYYY"
)

if isinstance(date_range, tuple) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = end_date = date_range

data = df[
    (df["Order_Date"].dt.date >= start_date) &
    (df["Order_Date"].dt.date <= end_date)
].copy()

if data.empty:
    st.warning("No data available for the selected dates.")
    st.stop()

sales = data["Sales"].sum()
profit = data["Profit"].sum()
orders = data["Order_ID"].nunique()
quantity = data["Quantity"].sum()
margin = profit / sales * 100 if sales else 0

st.markdown("""
<style>
[data-testid="stMetric"] {
    background-color: #f8fafc;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 14px 12px;
    min-height: 105px;
}
[data-testid="stMetricLabel"] {
    font-size: 14px !important;
    font-weight: 600 !important;
}
[data-testid="stMetricValue"] {
    font-size: 20px !important;
    font-weight: 700 !important;
    white-space: nowrap !important;
    overflow: visible !important;
}
</style>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
c1.metric("Total Sales", f"₹{sales:,.2f}")
c2.metric("Total Profit", f"₹{profit:,.2f}")
c3.metric("Orders", f"{orders:,}")

c4, c5 = st.columns(2)
c4.metric("Units Sold", f"{quantity:,.0f}")
c5.metric("Profit Margin", f"{margin:.2f}%")

st.caption(f"{start_date.strftime('%d %b %Y')} → {end_date.strftime('%d %b %Y')} | {len(data):,} records")
st.divider()

tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Overview", "🌍 Regional Analysis", "🛍️ Product Analysis", "📋 Data"
])

colors = px.colors.qualitative.Bold

with tab1:
    left, right = st.columns(2)

    monthly = (
        data.groupby("Month_Year", as_index=False)
        .agg(Sales=("Sales", "sum"))
        .sort_values("Month_Year")
    )

    with left:
        fig = px.line(monthly, x="Month_Year", y="Sales",
                      markers=True, title="Monthly Sales Trend")
        fig.update_traces(
            line=dict(color="#2563EB", width=4),
            marker=dict(size=9, color="#F97316")
        )
        fig.update_layout(xaxis_title="Month", yaxis_title="Sales (₹)")
        st.plotly_chart(fig, use_container_width=True)

    category = data.groupby("Category", as_index=False)["Sales"].sum()

    with right:
        fig = px.bar(category, x="Category", y="Sales",
                     color="Category", color_discrete_sequence=colors,
                     text="Sales", title="Sales by Category")
        fig.update_traces(texttemplate="%{text:.3s}")
        fig.update_layout(showlegend=False, yaxis_title="Sales (₹)")
        st.plotly_chart(fig, use_container_width=True)

    left, right = st.columns(2)

    segment = data.groupby("Segment", as_index=False)["Sales"].sum()
    with left:
        fig = px.pie(segment, names="Segment", values="Sales",
                     hole=0.45, color_discrete_sequence=px.colors.qualitative.Set2,
                     title="Sales by Segment")
        fig.update_traces(textinfo="label+percent")
        st.plotly_chart(fig, use_container_width=True)

    payment = data.groupby("Payment_Mode", as_index=False)["Sales"].sum()
    with right:
        fig = px.bar(payment, x="Payment_Mode", y="Sales",
                     color="Payment_Mode",
                     color_discrete_sequence=px.colors.qualitative.Pastel,
                     text="Sales", title="Sales by Payment Mode")
        fig.update_traces(texttemplate="%{text:.3s}")
        fig.update_layout(showlegend=False, yaxis_title="Sales (₹)")
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    region = (
        data.groupby("Region", as_index=False)
        .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
    )

    left, right = st.columns(2)

    with left:
        fig = px.bar(region, x="Region", y="Sales",
                     color="Region", color_discrete_sequence=colors,
                     text="Sales", title="Sales by Region")
        fig.update_traces(texttemplate="%{text:.3s}")
        fig.update_layout(showlegend=False, yaxis_title="Sales (₹)")
        st.plotly_chart(fig, use_container_width=True)

    with right:
        fig = px.bar(region, x="Region", y="Profit",
                     color="Region",
                     color_discrete_sequence=px.colors.qualitative.Set2,
                     text="Profit", title="Profit by Region")
        fig.update_traces(texttemplate="%{text:.3s}")
        fig.update_layout(showlegend=False, yaxis_title="Profit (₹)")
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Regional Performance")
    st.dataframe(region, use_container_width=True, hide_index=True)

with tab3:
    product = (
        data.groupby("Product", as_index=False)
        .agg(Sales=("Sales", "sum"),
             Profit=("Profit", "sum"),
             Quantity=("Quantity", "sum"),
             Orders=("Order_ID", "nunique"))
        .sort_values("Sales", ascending=False)
    )

    left, right = st.columns(2)

    with left:
        top10 = product.head(10).sort_values("Sales")
        fig = px.bar(top10, x="Sales", y="Product",
                     orientation="h", color="Sales",
                     color_continuous_scale="Turbo",
                     text="Sales", title="Top 10 Products by Sales")
        fig.update_traces(texttemplate="%{text:.3s}")
        fig.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig, use_container_width=True)

    with right:
        fig = px.scatter(
            data, x="Sales", y="Profit", size="Quantity",
            color="Category", color_discrete_sequence=colors,
            hover_data=["Product", "Region", "Segment"],
            title="Sales vs Profit"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Product Performance")
    st.dataframe(product, use_container_width=True, hide_index=True)

with tab4:
    st.subheader("Filtered Dataset")
    st.dataframe(data, use_container_width=True, hide_index=True)
    st.download_button(
        "⬇️ Download Filtered CSV",
        data.to_csv(index=False).encode("utf-8"),
        "filtered_sales_data.csv",
        "text/csv"
    )
