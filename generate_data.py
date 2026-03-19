import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def create_demand_data():
    # Generate 2 years of monthly dates
    dates = pd.date_range(start='2024-01-01', periods=24, freq='MS')
    
    # Create a trend: Demand grows slightly over time with some "noise"
    base_demand = 500
    growth = np.arange(24) * 15
    noise = np.random.normal(0, 50, 24)
    
    demand = base_demand + growth + noise
    
    df = pd.DataFrame({'Month': dates, 'Demand_Units': demand.astype(int)})
    df.to_csv('foundation_demand.csv', index=False)
    print("✅ Created 'foundation_demand.csv' with 24 months of data.")

if __name__ == "__main__":
    create_demand_data()