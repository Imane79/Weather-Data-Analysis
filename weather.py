import os
import pandas as pd


def process_weather_data(file_path):
    """
    Load and preprocess the weather dataset.
    - Converts 'time' to datetime.
    - Interpolates missing values for numeric columns.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The file {file_path} does not exist. Please verify the path.")

    # Load the dataset
    data = pd.read_csv(file_path)

    # Check if 'time' column exists
    if 'time' not in data.columns:
        raise KeyError(
            "The 'time' column is missing from the dataset. Ensure it exists and is correctly named.")

    # Convert 'time' column to datetime format
    data['time'] = pd.to_datetime(data['time'])

    # Interpolate missing numeric values
    numeric_columns = data.select_dtypes(include=['float', 'int']).columns
    data[numeric_columns] = data[numeric_columns].interpolate(
        method='linear', limit_direction='both')

    return data
