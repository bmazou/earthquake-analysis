# Earthquake Analysis

**[View the full report here](https://bmazou.github.io/earthquake-analysis/)**

This repository contains data processing scripts and a Quarto project for analyzing and visualizing earthquake data.

## Getting Started


Follow these steps to set up the project, preprocess the data, and render the final report.

### 1. Download the Dataset

1. Download the dataset from Kaggle: [All the Earthquakes Dataset: from 1990-2023](https://www.kaggle.com/datasets/alessandrolobello/the-ultimate-earthquake-dataset-from-1990-2023)
2. Extract the archive and place the `earthquakes.csv` file into the `data/` directory.

*(Note: The `data/` directory also contains tectonic plate boundary shapefiles (`PB2002_boundaries.shp`) which are required for mapping).*

- The tectonic plate boundary data comes from https://github.com/fraxen/tectonicplates

### 2. Set up the Environment

Create and activate a Python virtual environment, then install the dependencies:

```bash
# Create a virtual environment
python -m venv venv

# Activate the environment (Linux/macOS)
source venv/bin/activate   # (Linux/macOS)
venv\Scripts\activate      # Windows

# Install required packages
pip install -r requirements.txt
```

### 3. Preprocess Data

```bash
# Clean and group the raw earthquake data
python cleanup_data.py
```

### 4. Render the Quarto Report

Once the data is processed, render the Quarto document to compile the final report. Ensure you have [Quarto installed](https://quarto.org/docs/get-started/) on your system:

```bash
quarto render earthquakes.qmd
```

This will generate the formatted output in your workspace.
