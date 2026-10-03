import pandas as pd

df = pd.read_csv("cleaned_dataset.csv")

print("Dataset Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

# important statistics
print("\n-- Stastistical Summary --")
print(df[["Quantity", "UnitPrice"]].describe())

# negative quantity check
negative_quantity = df[df["Quantity"] < 0]

print("\n-- Negative Quantity Analysis --")
print("Negative Quantity records:", len(negative_quantity))
print("Total Negative Quantity:", negative_quantity["Quantity"].sum())

# Extreme quantity check
print("\n--- Highest Quantity Values ---")
print(df.nlargest(10,"Quantity")[["InvoiceNo", "StockCode", "Description", "Quantity"]])

# extreme negative quantity check
print("\n--- Lowest Quantity Values ---")
print(df.nsmallest(10,"Quantity")[["InvoiceNo", "StockCode", "Description", "Quantity"]])

# extreme unit price check
print("\n--- Highest Unit Price Values ---")
print(df.nlargest(10, "UnitPrice")[["InvoiceNo", "StockCode", "Description", "UnitPrice"]])

# extreme negative unit price check
print("\n--- Lowest Unit Price Values ---")
print(df.nsmallest(10,"UnitPrice")[["InvoiceNo", "StockCode", "Description", "UnitPrice"]])


# country-wise analysis
print("\n--- Top 10 countries by Transaction ---")
country_counts = df["Country"].value_counts().head(10)
print(country_counts)

import matplotlib.pyplot as plt

# top 10 countries by transaction plot
country_counts.plot(kind="bar", figsize = (10,6))

plt.title("Top 10 Counteries by Number of Transection")
plt.xlabel("Country")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("top_10_countries.png")
plt.show()

# Monthly transaction analysis
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

monthly_transactions = df.groupby(df["InvoiceDate"].dt.to_period("M")).size()

print("\n--- Monthly Transaction Analysis ---")
print(monthly_transactions)

# Monthly transaction chart
monthly_transactions.plot(kind="line", figsize=(10,6))

plt.title("Monthly Transactions")
plt.xlabel("Month")
plt.ylabel("Number of Transactions")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("monthly_transactions.png")
plt.show()



# Revenue analysis
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

total_revenue = df["Revenue"].sum()
print("\n--- Total Revenue ---")
print("Total Revenue: £", total_revenue)

# monthly revenue analysis
monthly_revenue = df.groupby(df["InvoiceDate"].dt.to_period("M"))["Revenue"].sum()
print("\n--- Monthly Revenue Analysis ---")
print(monthly_revenue)

#  Monthly revenue chart
monthly_revenue.plot(kind="bar", figsize=(12,5))

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("monthly_revenue.png")
plt.show()


# Top 10 products by revenue
product_revenue = df.groupby("Description")["Revenue"].sum().sort_values(ascending=False).head(10)
print("\n--- Top 10 Products by Revenue ---")
print(product_revenue)
# Top 10 products by revenue chart
product_revenue.plot(kind="barh", figsize=(10,6))
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product Description")
plt.tight_layout()
plt.savefig("top_10_products_revenue.png")
plt.show()


# Top 10 countries by revenue
country_revenue = df.groupby("Country")["Revenue"].sum().sort_values(ascending=False).head(10)
print("\n--- Top 10 Countries by Revenue ---")
print(country_revenue)
# Top 10 countries by revenue chart
country_revenue.plot(kind="bar", figsize=(10,5))
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.savefig("top_10_countries_revenue.png")
plt.show()

# Average revenue per transaction
average_transaction_value = df["Revenue"].mean()
print("\n--- Average Transection value ---")
print("Average Transaction Value: £", round(average_transaction_value, 2))

# UK revenue contribution
uk_revenue = df[df["Country"] == "United Kingdom"]["Revenue"].sum()
uk_percentage = (uk_revenue / total_revenue) * 100

print("\n--- UK Revenue Contribution ---")
print("UK Revenue: £", round(uk_revenue, 2))
print("UK Revenue Percentage:", round(uk_percentage, 2), "%")