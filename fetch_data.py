import pandas as pd

url = "https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv"

# Try with ISO-8859-1 encoding
df = pd.read_csv(url, encoding='ISO-8859-1')

print("Data Preview:")
print(df.head())

df.to_csv("sales_data.csv", index=False)
print("\nCSV file saved as 'sales_data.csv'")
