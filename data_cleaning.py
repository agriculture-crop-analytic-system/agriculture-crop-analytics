"""
Clean the agriculture crop analytics dataset.
Run: python data_cleaning.py
"""
import pandas as pd

INPUT_FILE = "agriculture_crop_analytics_500_rows.csv"
OUTPUT_FILE = "clean_dataset.csv"

def clean_data(input_file=INPUT_FILE, output_file=OUTPUT_FILE):
    """Remove empty index columns and duplicates, then fill missing values."""
    data = pd.read_csv(input_file)
    data = data.loc[:, ~data.columns.astype(str).str.startswith("Unnamed")]
    data = data.drop_duplicates()

    for column in data.columns:
        if pd.api.types.is_numeric_dtype(data[column]):
            data[column] = data[column].fillna(data[column].median())
        else:
            mode = data[column].mode(dropna=True)
            if not mode.empty:
                data[column] = data[column].fillna(mode.iloc[0])

    data.to_csv(output_file, index=False)
    print(f"Cleaned dataset saved as {output_file}")
    print(f"Rows: {len(data)}, Columns: {len(data.columns)}")
    return data

if __name__ == "__main__":
    clean_data()
