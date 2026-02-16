import pandas as pd
import numpy as np
import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import os

def run_shap_analysis():
    print("Loading Birhan Energies data...")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.abspath(os.path.join(base_dir, '../data/brentoilprices.csv'))
    
    # 1. Load and Clean Data
    df = pd.read_csv(data_path)
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y', errors='coerce')
    df = df.dropna().sort_values('Date').reset_index(drop=True)
    
    # 2. Financial Feature Engineering
    # Finance sectors rely on lag and volatility to assess risk
    df['Price_Lag_1'] = df['Price'].shift(1)
    df['Price_Lag_7'] = df['Price'].shift(7)
    df['Rolling_Vol_30'] = df['Price'].rolling(window=30).std()
    df['Daily_Return'] = df['Price'].pct_change()
    
    # Drop NaNs created by lagging/rolling
    df = df.dropna()
    
    # Define Features (X) and Target (y) - Predicting tomorrow's price
    features = ['Price_Lag_1', 'Price_Lag_7', 'Rolling_Vol_30', 'Daily_Return']
    X = df[features]
    y = df['Price']
    
    # 3. Train a Random Forest Model
    print("Training Risk Model...")
    model = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=5)
    model.fit(X, y)
    
    # 4. Generate SHAP Explanations
    print("Generating SHAP Explainability Plot...")
    explainer = shap.TreeExplainer(model)
    # Use a sample of 500 records for fast computation
    X_sample = X.tail(500) 
    shap_values = explainer.shap_values(X_sample)
    
    # 5. Save the Plot
    plt.figure(figsize=(10, 6))
    shap.summary_plot(shap_values, X_sample, show=False)
    
    # Save to the docs folder for your final report
    output_path = os.path.abspath(os.path.join(base_dir, '../docs/shap_summary.png'))
    plt.title('SHAP Feature Importance: Brent Oil Risk Factors', fontsize=14)
    plt.tight_layout()
    plt.savefig(output_path)
    print(f"Success! SHAP plot saved to: {output_path}")

if __name__ == "__main__":
    run_shap_analysis()