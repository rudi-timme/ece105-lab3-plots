# Sensor Plot Generator

A small Python script that generates synthetic temperature sensor data and produces publication-ready scatter, histogram, and box plot visualizations.

## Installation

1. Activate the `ece105` conda environment:

    ```bash
    conda activate ece105
    ```

2. Install the required packages using conda or mamba:

    ```bash
    conda install numpy matplotlib -y
    ```

    or

    ```bash
    mamba install numpy matplotlib -y
    ```

## Usage

Run the script from the project directory:

```bash
python generate_plots.py
```

## Example output

The script produces a single image file named `sensor_analysis.png` containing three subplots:

- A scatter plot of Sensor A and Sensor B temperature readings over time.
- An overlaid histogram comparing the temperature distributions of both sensors.
- A side-by-side box plot comparing the spread and medians of the two sensors.

## AI tools used and disclosure

This README was generated with the assistance of AI tooling. Please replace this paragraph with your own disclosure details and any relevant attribution.
