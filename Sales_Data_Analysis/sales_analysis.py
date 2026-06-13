
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "sales_data.csv")

# Read CSV file
data = pd.read_csv(csv_path)

print("Sales Data:")
print(data)

# Total Sales
total_sales = data["Sales"].sum()
print("\nTotal Sales:", total_sales)

# Sales by Product
product_sales = data.groupby("Product")["Sales"].sum()

print("\nSales by Product:")
print(product_sales)

# Best Selling Product
best_product = product_sales.idxmax()

print("\nBest Selling Product:", best_product)


# Highest Revenue
highest_sales = product_sales.max()

print("Highest Revenue:", highest_sales)

import matplotlib.pyplot as plt

product_sales.plot(kind="bar")

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()

# Monthly Sales Analysis
monthly_sales = data.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Best Month
best_month = monthly_sales.idxmax()

print("\nBest Month:", best_month)

# Save Report

report_path = os.path.join(BASE_DIR, "sales_report.csv")

monthly_sales.to_csv(report_path)

print("Saved at:", report_path)