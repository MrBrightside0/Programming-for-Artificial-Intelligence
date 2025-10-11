import pandas as pd
import os

def load_data(path):
    """Loads the dataset from a CSV file."""
    df = pd.read_csv(path)
    print(f"📂 File loaded successfully: {len(df)} records, {len(df.columns)} columns.")
    return df

def clean_data(df):
    """Removes duplicates, empty rows, and standardizes column names."""
    print("\n🧹 Cleaning data...")
    df = df.drop_duplicates()
    df = df.dropna(how='all')
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    print("✅ Data cleaned successfully.")
    return df

def save_results(tables, base_path):
    """Saves each normalized table into a CSV file."""
    os.makedirs(base_path, exist_ok=True)
    for name, table in tables.items():
        table.to_csv(f"{base_path}/{name}.csv", index=False)
    print("💾 Normalized tables saved successfully.")

def save_results(tables, base_path):
    """Saves each normalized table into a CSV file."""
    os.makedirs(base_path, exist_ok=True)
    for name, table in tables.items():
        table.to_csv(f"{base_path}/{name}.csv", index=False)
        print(f"✅ {name}.csv → {len(table)} rows, {len(table.columns)} columns")
    print("💾 Normalized tables saved successfully.")
