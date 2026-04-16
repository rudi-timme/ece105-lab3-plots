"""Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage
-----
    python generate_plots.py
"""

# Create a function generate_data(seed) that returns sensor_a, sensor_b,
# and timestamps arrays with the same parameters as in the notebook.
# Use NumPy-style docstring with Parameters and Returns sections.

import numpy as np
import matplotlib.pyplot as plt


def generate_data(seed):
    """Generate synthetic temperature sensor data.

    Parameters
    ----------
    seed : int
        Seed value for NumPy random number generation.

    Returns
    -------
    sensor_a : numpy.ndarray
        Array of shape (200,) containing Sensor A temperature readings in Celsius.
    sensor_b : numpy.ndarray
        Array of shape (200,) containing Sensor B temperature readings in Celsius.
    timestamps : numpy.ndarray
        Array of shape (200,) containing timestamps uniformly sampled from 0 to 10 seconds.
    """
    rng = np.random.default_rng(seed)
    n_readings = 200

    timestamps = rng.uniform(0.0, 10.0, size=n_readings)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=n_readings)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=n_readings)

    order = np.argsort(timestamps)
    timestamps = timestamps[order]
    sensor_a = sensor_a[order]
    sensor_b = sensor_b[order]

    return sensor_a, sensor_b, timestamps


# Create plot_scatter(sensor_a, sensor_b, timestamps, ax) that draws
# the scatter plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Draw a sensor temperature scatter plot on an existing Axes.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A temperature readings of shape (200,), in Celsius.
    sensor_b : numpy.ndarray
        Sensor B temperature readings of shape (200,), in Celsius.
    timestamps : numpy.ndarray
        Timestamp values of shape (200,), in seconds.
    ax : matplotlib.axes.Axes
        Axes object to draw the scatter plot on.

    Returns
    -------
    None
        The function modifies the provided Axes object in place.
    """
    ax.scatter(timestamps, sensor_a, color="tab:blue", alpha=0.7, label="Sensor A")
    ax.scatter(timestamps, sensor_b, color="tab:orange", alpha=0.7, label="Sensor B")
    ax.set_title("Sensor Temperature Readings vs Time")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.5)


# Create plot_histogram(sensor_a, sensor_b, timestamps, ax) that draws
# the histogram from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_histogram(sensor_a, sensor_b, timestamps, ax):
    """Draw an overlaid temperature histogram for Sensor A and Sensor B.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A temperature readings of shape (200,), in Celsius.
    sensor_b : numpy.ndarray
        Sensor B temperature readings of shape (200,), in Celsius.
    timestamps : numpy.ndarray
        Timestamp values of shape (200,), in seconds. This argument is kept for
        API consistency but not used in the histogram itself.
    ax : matplotlib.axes.Axes
        Axes object to draw the histogram on.

    Returns
    -------
    None
        The function modifies the provided Axes object in place.
    """
    ax.hist(sensor_a, bins=30, color="tab:blue", alpha=0.5, label="Sensor A")
    ax.hist(sensor_b, bins=30, color="tab:orange", alpha=0.5, label="Sensor B")

    mean_a = np.mean(sensor_a)
    mean_b = np.mean(sensor_b)
    ax.axvline(mean_a, color="tab:blue", linestyle="--", linewidth=2, label="Mean A")
    ax.axvline(mean_b, color="tab:orange", linestyle="--", linewidth=2, label="Mean B")

    ax.set_title("Temperature Distribution for Sensor A and Sensor B")
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Frequency")
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.4)


# Create plot_boxplot(sensor_a, sensor_b, timestamps, ax) that draws
# the box plot from the notebook onto the given Axes object.
# NumPy-style docstring. Modifies ax in place, returns None.

def plot_boxplot(sensor_a, sensor_b, timestamps, ax):
    """Draw a side-by-side box plot comparing Sensor A and Sensor B.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A temperature readings of shape (200,), in Celsius.
    sensor_b : numpy.ndarray
        Sensor B temperature readings of shape (200,), in Celsius.
    timestamps : numpy.ndarray
        Timestamp values of shape (200,), in seconds. This argument is kept for
        API consistency but not used in the box plot itself.
    ax : matplotlib.axes.Axes
        Axes object to draw the box plot on.

    Returns
    -------
    None
        The function modifies the provided Axes object in place.
    """
    ax.boxplot([sensor_a, sensor_b], labels=["Sensor A", "Sensor B"], patch_artist=True,
               boxprops=dict(facecolor="lightgray", color="black"),
               medianprops=dict(color="red"),
               whiskerprops=dict(color="black"),
               capprops=dict(color="black"))

    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))
    ax.axhline(overall_mean, color="blue", linestyle="--", linewidth=1.5,
               label=f"Overall Mean = {overall_mean:.2f} °C")

    ax.set_title("Sensor Temperature Distribution Comparison")
    ax.set_ylabel("Temperature (deg C)")
    ax.legend()
    ax.grid(axis="y", linestyle="--", alpha=0.4)


# Create main() that generates data, creates a 1x3 subplot figure,
# calls each plot function, adjusts layout, and saves as sensor_analysis.png
# at 150 DPI with tight bounding box.

def main():
    """Generate sensor data, create plots, and save the resulting figure.

    This function generates synthetic sensor data using a fixed seed,
    creates a 1x3 figure containing scatter, histogram, and box plots,
    adjusts the layout for readability, and saves the figure to disk.

    Returns
    -------
    None
        The function saves the figure to ``sensor_analysis.png`` and does not
        return any value.
    """
    seed = 9658
    sensor_a, sensor_b, timestamps = generate_data(seed)

    fig, axs = plt.subplots(1, 3, figsize=(18, 5))
    plot_scatter(sensor_a, sensor_b, timestamps, axs[0])
    plot_histogram(sensor_a, sensor_b, timestamps, axs[1])
    plot_boxplot(sensor_a, sensor_b, timestamps, axs[2])

    fig.tight_layout()
    fig.savefig("sensor_analysis.png", dpi=150, bbox_inches="tight")


if __name__ == "__main__":
    main()


