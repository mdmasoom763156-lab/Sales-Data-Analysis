# Sales Data Analysis Report

## Project Overview

This project is a simple Sales Data Analysis program built using Python and the pandas library.

The program reads sales data from a CSV file and analyzes the dataset to calculate important sales metrics such as total sales, average sales, highest sales, and the best-selling product.



## Objectives

The main objectives of this project are:

- Load CSV data using pandas
- Analyze sales data efficiently
- Calculate important sales metrics
- Identify the best-selling product
- Practice data analysis using Python

---

## Analysis Steps

The following steps were performed in this project:

1. Loaded the CSV file using pandas
2. Displayed the first few rows of the dataset
3. Checked dataset structure and column names
4. Calculated total sales
5. Calculated average sales
6. Found the highest sales value
7. Identified the best-selling product

---

## Metrics Calculated

The project calculates:

- Total Sales
- Average Sales
- Highest Sales
- Best-Selling Product

---

## Technologies Used

- Python
- Pandas
- VS Code

---

## Python Concepts Used

- Variables
- Functions
- CSV file handling
- DataFrames
- Data analysis using pandas

---

## Example Code

```python
import pandas as pd

# Read CSV file
df = pd.read_csv("sales_data.csv")

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Display first rows
print(df.head())

# Sales calculations
total_sales = df["total_sales"].sum()
average_sales = df["total_sales"].mean()
highest_sales = df["total_sales"].max()

# Best-selling product
best_product = df.loc[df["total_sales"].idxmax(), "product"]

# Display report
print("\nSALES REPORT")
print("_______________")
print("Total Sales   :", total_sales)
print("Average Sales :", average_sales)
print("Highest Sales :", highest_sales)
print("Best Product  :", best_product)