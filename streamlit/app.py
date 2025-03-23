# streamlit_app/app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import os

# 📐 Page config
st.set_page_config(layout="wide", page_title="Walmart Sales Forecasting")

# 📥 Load forecast summary
summary_path = 'forecasts/forecast_summary.csv'
try:
    summary_df = pd.read_csv(summary_path)
except FileNotFoundError:
    st.error("❌ Forecast summary file not found. Please ensure 'forecast_summary.csv' exists in the 'forecasts' folder.")
    st.stop()

st.title("📈 Walmart Sales Forecasting App")
st.markdown("""
Select a **Store** and **Department** to view forecast results. Use the date filter and insights panel to explore trends, risks, and suggested actions.
---
""")

# 🏆 Top 5 best-performing forecasts
st.sidebar.subheader("🏆 Top 5 Most Accurate Forecasts")
top5 = summary_df.sort_values('MAPE').head(5)
st.sidebar.dataframe(top5[['Store', 'Dept', 'MAPE', 'RMSE']])

# Sidebar for store and dept selection
st.sidebar.markdown("---")
st.sidebar.subheader("🔎 Select Store & Department")
stores = sorted(summary_df['Store'].unique())
depts = sorted(summary_df['Dept'].unique())

selected_stores = st.sidebar.multiselect("Select Store(s):", stores, default=[stores[0]])
selected_depts = st.sidebar.multiselect("Select Department(s):", depts, default=[depts[0]])

# Iterate through all selected combinations
for store in selected_stores:
    for dept in selected_depts:
        st.markdown(f"## 📍 Store {store} – Dept {dept} Forecast")

        file_name = f"forecasts/Store{store}_Dept{dept}_forecast.csv"
        if not os.path.exists(file_name):
            st.warning(f"⚠️ Forecast file not found for Store {store}, Dept {dept}.")
            continue

        df = pd.read_csv(file_name, parse_dates=['ds'])

        # 📊 KPIs
        mape = summary_df[(summary_df['Store'] == store) & (summary_df['Dept'] == dept)]['MAPE'].values[0]
        rmse = summary_df[(summary_df['Store'] == store) & (summary_df['Dept'] == dept)]['RMSE'].values[0]

        col1, col2 = st.columns(2)
        col1.metric("MAPE", f"{mape}%")
        col2.metric("RMSE", f"{rmse}")

        # 📅 Date filtering
        st.markdown("### 📅 Filter Date Range")
        min_date, max_date = df['ds'].min(), df['ds'].max()
        date_range = st.date_input(
            "Select date range:", [min_date, max_date], min_value=min_date, max_value=max_date, key=f"date_{store}_{dept}")

        filtered_df = df[(df['ds'] >= pd.to_datetime(date_range[0])) & (df['ds'] <= pd.to_datetime(date_range[1]))]

        # 📊 Plot with Plotly
        fig = px.line(filtered_df, x='ds', y=['y', 'yhat'],
                      labels={'value': 'Weekly Sales', 'ds': 'Date'},
                      title=f"Forecast vs Actual – Store {store}, Dept {dept}")
        fig.update_traces(mode='lines+markers')
        fig.update_layout(legend_title_text='Legend')
        st.plotly_chart(fig, use_container_width=True)

        # 📄 Raw Data
        with st.expander("📄 Show forecast data"):
            st.dataframe(filtered_df.tail(30))

        # 📈 Insight Summary
        st.markdown("### 📌 Insights & Suggested Actions")
        actual_total = filtered_df['y'].sum()
        forecast_total = filtered_df['yhat'].sum()
        change_pct = ((forecast_total - actual_total) / actual_total) * 100

        if change_pct > 5:
            trend = "📈 Forecasted increase in sales. Consider increasing inventory or promotional campaigns."
        elif change_pct < -5:
            trend = "📉 Forecasted decline in sales. Investigate possible demand drops or operational issues."
        else:
            trend = "➡️ Sales expected to remain stable. Maintain current strategies."

        st.info(f"**Trend Insight**: {trend}")
        st.markdown(f"**Total Forecasted Sales**: ${forecast_total:,.0f}  ")
        st.markdown(f"**Actual Sales in Range**: ${actual_total:,.0f}  ")
        st.markdown(f"**Change**: {change_pct:.2f}%")

        # ⬇️ Download CSV
        st.download_button(
            label="📥 Download Forecast CSV",
            data=filtered_df.to_csv(index=False),
            file_name=f"Store{store}_Dept{dept}_forecast.csv",
            mime='text/csv',
            key=f"dl_{store}_{dept}"
        )

st.markdown("---")
st.caption("Developed by [Your Name] | Streamlit Forecasting App | © 2025")
