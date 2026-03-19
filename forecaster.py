import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

class DemandForecaster:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.df['Month_Index'] = np.arange(len(self.df)) # Convert dates to numbers 0, 1, 2...

    def train_model(self):
        # X = Month Index, y = Demand
        X = self.df[['Month_Index']]
        y = self.df['Demand_Units']
        
        self.model = LinearRegression()
        self.model.fit(X, y)
        print("✅ Model trained on historical demand trends.")

    def predict_next_month(self):
        next_month_idx = np.array([[len(self.df)]])
        prediction = self.model.predict(next_month_idx)
        return round(prediction[0], 2)

if __name__ == "__main__":
    forecaster = DemandForecaster('foundation_demand.csv')
    forecaster.train_model()
    result = forecaster.predict_next_month()
    print(f"🚀 Predicted Demand for Next Month: {result} Units")