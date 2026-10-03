# SWYNEX - Exploratory Data Analysis

## 📌 Project Overview

This project focuses on Exploratory Data Analysis (EDA) of an online retail dataset using Python.

The cleaned dataset prepared during Task 1 was analyzed to understand important statistics, trends, patterns, revenue distribution, and potential anomalies.

The analysis helps identify customer transaction patterns, monthly performance, product revenue, country-wise performance, and unusual values in the dataset.

---

## 🎯 Objectives

- Perform Exploratory Data Analysis on the cleaned dataset.
- Calculate important statistical measures.
- Identify trends and patterns in transactions.
- Analyze revenue across months, countries, and products.
- Detect potential anomalies in quantity and unit price.
- Extract at least five useful business insights.
- Visualize important findings using charts.

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- Matplotlib
- VS Code
- CSV Dataset

---

## 📂 Project Structure

```text
SWYNEX-Exploratory-Data-Analysis/
│
├── cleaned_dataset.csv
├── eda_analysis.py
├── top_10_countries.png
├── monthly_transactions.png
├── monthly_revenue.png
├── top_10_products_revenue.png
├── top_10_countries_revenue.png
└── README.md
```

---

## 📊 Analysis Performed

### 1. Statistical Analysis

Calculated important statistics for:

- Quantity
- Unit Price
- Mean
- Median
- Minimum
- Maximum
- Standard deviation

### 2. Quantity & Anomaly Analysis

Analyzed negative and extreme quantity values to identify possible returns, cancellations, or unusual transactions.

### 3. Unit Price Analysis

Examined the minimum and maximum unit prices and identified unusual or non-standard transaction values.

### 4. Country Analysis

Analyzed the number of transactions for different countries and identified countries with the highest transaction counts.

### 5. Monthly Transaction Analysis

Analyzed transaction activity across different months to identify periods of high and low activity.

### 6. Revenue Analysis

Calculated revenue using:

**Revenue = Quantity × UnitPrice**

The calculated total revenue was approximately **£8.28 million**.

### 7. Product Analysis

Identified the top products based on calculated revenue.

### 8. Country-wise Revenue Analysis

Compared calculated revenue across different countries.

### 9. Average Transaction Value

The average calculated transaction value was approximately **£20.62**.

---

## 💡 Key Insights

### 1. UK Dominates Transactions and Revenue

The United Kingdom recorded **356,704 transaction records** and contributed approximately **81.5% of the calculated revenue**.

### 2. November 2011 Had the Highest Transaction Activity

November 2011 recorded approximately **64,218 transaction records**, making it the highest-activity month in the analyzed period.

### 3. November 2011 Also Had the Highest Monthly Revenue

The calculated revenue for November 2011 was approximately **£1.13 million**, making it the highest monthly revenue period in the analysis.

### 4. Negative Quantities Indicate Potential Returns or Cancellations

There were **8,872 records with negative quantities**, with a combined quantity of approximately **-273,035 units**.

These records may represent returns, cancellations, or other adjustment transactions.

### 5. Extreme Values Require Further Investigation

Quantity values ranged from approximately **-80,995 to 80,995**, while UnitPrice ranged from **£0.001 to £38,970**.

These extreme values may represent unusual or non-standard transactions and should be investigated further before being used for certain business decisions.

---

## 📈 Visualizations

The project includes the following charts:

- Top 10 Countries by Number of Transactions
- Monthly Transactions
- Monthly Revenue
- Top 10 Products by Revenue
- Top 10 Countries by Revenue

---

## 📌 Conclusion

The exploratory analysis provided useful insights into transaction activity, revenue patterns, country-wise performance, product performance, and potential anomalies in the online retail dataset.

Python, Pandas, and Matplotlib were used to perform the analysis and create visualizations.

The analysis demonstrates how Exploratory Data Analysis can be used to transform raw data into meaningful business insights.

---

## 👩‍💻 Internship Task

**Organization:** SWYNEX Technologies  
**Task:** Exploratory Data Analysis  
**Domain:** Data Analytics