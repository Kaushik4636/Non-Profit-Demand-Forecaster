# Non-Profit Resource Demand Forecaster 📊

A predictive analytics tool built to optimize supply chain efficiency for non-profit organizations and foundations (Inspired by fieldwork with Dr. Reddy’s Foundation).

## 🚀 The Problem
Non-profits often face "Resource Mismatch"—sending too much or too little aid to specific regions due to a lack of data-driven forecasting. This leads to wastage or, worse, underserving communities in need.

## 💡 The Solution
This project implements a **Time-Series Forecasting Model** using Linear Regression to predict monthly resource requirements. By analyzing historical demand patterns, the model provides a "Data-First" approach to logistics and planning.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Modeling:** Scikit-Learn (Linear Regression)
- **Data Manipulation:** Pandas & NumPy
- **Visualization:** Matplotlib

## 📈 Key Features
- **Trend Analysis:** Identifies growth or decline in resource needs over a 24-month period.
- **Automated Prediction:** Calculates specific unit requirements for the upcoming month with high statistical confidence.
- **Data Storytelling:** Generates a visual "Trend Line" (found in `demand_forecast_chart.png`) to help non-technical stakeholders understand future needs.

## 📂 Project Structure
- `generate_data.py`: Simulates 2 years of foundation demand data.
- `forecaster.py`: The machine learning logic for training and prediction.
- `plotter.py`: Generates the visual performance chart.
- `demand_forecast_chart.png`: The final visualization of the model's accuracy.

## ⚙️ How to Run
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Generate data: `python generate_data.py`
4. Run the forecast and see the chart: `python plotter.py`
