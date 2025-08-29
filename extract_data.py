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


# เพิ่มโค้ดส่วนนี้เข้าไปในไฟล์ extract_data.py
def load_data_to_csv(df, output_path):
    """Loads a DataFrame to a CSV file."""
    try:
        df.to_csv(output_path, index=False)
        print(f"Data loaded successfully to {output_path}")
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
