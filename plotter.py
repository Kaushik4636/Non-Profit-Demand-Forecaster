import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from forecaster import DemandForecaster

# 1. Load data and the model
forecaster = DemandForecaster('foundation_demand.csv')
forecaster.train_model()
prediction = forecaster.predict_next_month()

# 2. Setup the Plot
plt.figure(figsize=(10, 6))
plt.scatter(forecaster.df['Month_Index'], forecaster.df['Demand_Units'], color='blue', label='Actual Historical Demand')

# 3. Draw the "Trend Line" (Regression Line)
X = forecaster.df[['Month_Index']]
plt.plot(X, forecaster.model.predict(X), color='red', linewidth=2, label='Forecast Trend Line')

# 4. Mark the Prediction for Next Month
next_idx = len(forecaster.df)
plt.scatter(next_idx, prediction, color='green', s=100, label=f'Next Month Prediction: {prediction}')

# 5. Add Labels & Style
plt.title('Non-Profit Resource Demand: Historical vs. Predicted', fontsize=14)
plt.xlabel('Months (Time)', fontsize=12)
plt.ylabel('Units Required', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# 6. Save and Show
plt.savefig('demand_forecast_chart.png')
print("✅ Chart saved as 'demand_forecast_chart.png'. Open it to see your work!")
plt.show()