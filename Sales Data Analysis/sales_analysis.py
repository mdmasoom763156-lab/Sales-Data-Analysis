import pandas as pd


df = pd.read_csv("sales_data.csv")


df.columns = df.columns.str.lower()


print(df.columns)


total_sales = df["total_sales"].sum()
average_sales = df["total_sales"].mean()
highest_sales = df["total_sales"].max()


best_product = df.loc[df["total_sales"].idxmax(), "product"]


print("\nSALES REPORT")
print("_______________")
print("Total Sales   :", total_sales)
print("Average Sales :", average_sales)
print("Highest Sales :", highest_sales)
print("Best Product  :", best_product)