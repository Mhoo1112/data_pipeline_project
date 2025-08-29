# extract_data.py
import pandas as pd

def extract_data_from_csv(file_path):
    """Extracts data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        print("Data extracted successfully.")
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None