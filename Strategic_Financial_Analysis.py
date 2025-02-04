import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dummy Data: Financial Statements
data = {
    "Year": [2021, 2022, 2023, 2024],
    "Revenue (in Cr)": [80, 100, 130, 160],
    "Expenses (in Cr)": [50, 65, 85, 110],
}

df = pd.DataFrame(data)
df["Profit (in Cr)"] = df["Revenue (in Cr)"] - df["Expenses (in Cr)"]

# Competitive Benchmarking Data
competitors = {
    "Company": ["Client", "Competitor A", "Competitor B", "Competitor C"],
    "Market Share (%)": [20, 35, 25, 20],
    "Annual Growth (%)": [15, 12, 18, 10],
    "Revenue (in Cr)": [160, 220, 190, 140],
}

competitor_df = pd.DataFrame(competitors)

# Investment Analysis
investment = 400  # in crores
expected_roi = [12, 15, 20, 18]  # ROI for 4 investment options

best_investment = max(expected_roi)
best_option_index = expected_roi.index(best_investment)
print(f"Recommended Investment Option {best_option_index + 1} with ROI: {best_investment}%")

# Financial Model Visualization (MIS Dashboard)
plt.figure(figsize=(8, 5))
plt.plot(df["Year"], df["Revenue (in Cr)"], label="Revenue", marker="o")
plt.plot(df["Year"], df["Expenses (in Cr)"], label="Expenses", marker="s")
plt.plot(df["Year"], df["Profit (in Cr)"], label="Profit", marker="^")
plt.xlabel("Year")
plt.ylabel("Amount (Cr)")
plt.title("Financial Performance Dashboard")
plt.legend()
plt.grid()
plt.show()

# Competitive Benchmarking Visualization
plt.figure(figsize=(8, 5))
plt.bar(competitor_df["Company"], competitor_df["Market Share (%)"], color=["blue", "red", "green", "orange"])
plt.xlabel("Company")
plt.ylabel("Market Share (%)")
plt.title("Competitive Benchmarking")
plt.show()

