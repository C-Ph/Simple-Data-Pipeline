# Simple-Data-Pipeline

This project demonstrates a simple data pipeline using Python and Pandas. The pipeline extracts data from a CSV file, processes the data, and stores the processed data in a new CSV file.

## Features
- **Data Extraction**: Loads data from a specified CSV file.
- **Data Processing**: Filters data based on conditions and adds a new column to indicate status (e.g., 'senior' or 'junior').
- **Data Storage**: Saves the processed data into a new CSV file.

## Why Use `file_path`?
Using a `file_path` parameter instead of hardcoding the filename increases flexibility. You can easily change the input file without modifying the code, making it reusable for different datasets.

The processed data will be saved in `processed_data.csv`.

## Installation
install the required library using pip:

```bash
pip install pandas
