# 🛍️ Walmart Sales Forecasting App

An interactive Streamlit app for forecasting Walmart’s weekly sales at the Store–Department level using time series models. This project enables business users to visualize future sales, compare actual vs predicted performance, and identify departments requiring inventory or demand planning adjustments.

---

## 🧠 Problem Statement

Walmart, as a large retail chain, needs accurate weekly sales forecasts to optimize inventory, staffing, and promotions across its stores. With over 45 stores and 80+ departments, manually forecasting each Store–Dept combination is time-consuming and prone to errors.

This app solves that problem by:
- Automating forecasts for each Store–Dept pair
- Providing an interactive UI for users to select and explore forecasts
- Displaying performance metrics like **MAPE** and **RMSE** to track model accuracy
- Offering downloadable CSV reports for operational teams

---

## 📊 Data Source

The dataset is from the [Walmart Recruiting - Store Sales Forecasting](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting) competition on Kaggle.

- **Columns include**:  
  - `Store`: Store ID  
  - `Dept`: Department ID  
  - `Date`: Weekly sales date  
  - `Weekly_Sales`: Actual sales  
  - `IsHoliday`: Whether the week contains a holiday  

---

## 🔮 Forecasting Method

We used Facebook's **Prophet** library to build univariate time series models for each Store–Dept pair.

### Why Prophet?
- Handles seasonality (weekly and yearly)
- Automatically detects holidays and trend shifts
- Great for business applications with interpretable output

Each model was trained on historical sales data and stored in the `forecasts/` directory. A summary table of forecast accuracy is stored in `forecast_summary.csv`.

---

## 📈 Model Performance

Performance is evaluated using:

- **MAPE (Mean Absolute Percentage Error)**
- **RMSE (Root Mean Squared Error)**

The 5 most accurate forecasts based on MAPE are displayed in the sidebar.

| Store | Dept | MAPE (%) | RMSE  |
|-------|------|----------|--------|
| 2     | 7    | 4.32     | 1290.2 |
| 4     | 3    | 5.01     | 1425.7 |
| 6     | 9    | 5.15     | 1532.6 |
| 20    | 1    | 5.42     | 1581.4 |
| 14    | 2    | 5.67     | 1650.3 |

---

## 🖼️ Screenshots of the App

### 🌐 Main UI
![Main App Screenshot](screenshots/main_ui.png)

### 📊 Forecast Chart
![Forecast Chart](screenshots/forecast_plot.png)

### 📄 Forecast Table + CSV Download
![Forecast Table](screenshots/forecast_table.png)


---

## 🚀 How to Run Locally

### 🔧 Prerequisites
- Python 3.8+
- `pip` or `conda` package manager

▶️ Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
Visit http://localhost:8501 in your browser.


✅ Features
Interactive Store & Department selection

MAPE & RMSE model metrics

Actual vs Forecasted sales visualization

Custom date range filter

Downloadable forecast CSVs

Sidebar leaderboard of best forecasts

🧠 Future Improvements
Add ARIMA and LSTM model comparison

Deploy via Docker or Streamlit Cloud

Include holiday impact analysis

Add inventory or promotion-based overlays

📌 License
This project is licensed under the MIT License. See the LICENSE file for more information.

🙌 Acknowledgements
Walmart Sales Forecasting Competition on Kaggle

Facebook Prophet




