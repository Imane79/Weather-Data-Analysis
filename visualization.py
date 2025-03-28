import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


def plot_weather_trends(data, columns, title):
    """
    Plot weather trends using cubic splines for smoother curves with improvements:
    - Separate subplots for each variable.
    - Aggregated data for reduced noise.
    - Enhanced aesthetics for readability.
    """
    # Aggregating data to weekly means for clarity
    data = data.resample('W', on='time').mean(
    ).reset_index()  # Reset index to retain 'time'

    # Set up subplots
    num_columns = len(columns)
    fig, axes = plt.subplots(num_columns, 1, figsize=(
        12, 6 * num_columns), sharex=True)

    if num_columns == 1:
        axes = [axes]  # Ensure axes is iterable even for a single subplot

    for ax, column in zip(axes, columns):
        # Generate cubic spline for smooth trends
        x = np.arange(len(data))
        y = data[column].values
        spline = CubicSpline(x, y)

        ax.plot(data['time'], spline(x), label=f"{column} Trend", linewidth=2)
        ax.set_title(f"{column} Trend", fontsize=14)
        ax.set_ylabel("Values", fontsize=12)
        ax.grid(alpha=0.6)
        ax.legend()

    # Shared x-axis label
    axes[-1].set_xlabel("Time", fontsize=12)

    # Main title for the plot
    fig.suptitle(title, fontsize=16, y=0.92)
    plt.tight_layout()
    plt.show()
