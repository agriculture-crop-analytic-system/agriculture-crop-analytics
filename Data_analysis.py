"""
Analyze the cleaned agriculture crop analytics dataset.
Run: python Data_analysis.py
"""
import pandas as pd

FILE = "clean_dataset.csv"

def analyze_data(file_name=FILE):
    """Print useful summary statistics and crop/state comparisons."""
    data = pd.read_csv(file_name)

    print("\n--- DATASET OVERVIEW ---")
    print("Rows and columns:", data.shape)
    print("\nMissing values:\n", data.isnull().sum())
    print("\nNumerical summary:\n", data.describe().round(2))

    print("\n--- AVERAGE YIELD BY CROP ---")
    print(data.groupby("Crop")["Yield_Tons"].mean().sort_values(ascending=False).round(2))

    print("\n--- TOTAL PROFIT BY STATE (TOP 10) ---")
    print(data.groupby("State")["Profit_INR"].sum().sort_values(ascending=False).head(10).round(2))

    print("\n--- AVERAGE PROFIT BY SEASON ---")
    print(data.groupby("Season")["Profit_INR"].mean().sort_values(ascending=False).round(2))

    print("\n--- DISEASE RISK COUNTS ---")
    print(data["Disease_Risk"].value_counts())

if __name__ == "__main__":
    analyze_data()
