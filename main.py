from weather import process_weather_data
from visualization import plot_weather_trends

# Path to the dataset
DATASET_PATH = "data/NYC_Weather_2016_2022 2.csv"

# Step 1: Process the dataset
weather_data = process_weather_data(DATASET_PATH)

# Step 2: Visualize weather trends
columns_to_plot = [
    'temperature_2m (°C)', 'precipitation (mm)', 'windspeed_10m (km/h)']
plot_weather_trends(weather_data, columns_to_plot,
                    "Weather Trends: Temperature, Precipitation, and Wind Speed")
