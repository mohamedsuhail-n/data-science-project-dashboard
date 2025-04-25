import pandas as pd

# Load raw dataset
df = pd.read_csv('sales_data.csv', encoding='ISO-8859-1')

# Step 1: Rename columns (custom names based on structure)
df.columns = [
    'id', 'date', 'region', 'sub_region', 'total_rent',
    'parking_fee', 'other_costs', 'total_cost',
    'user_count', 'avg_temp', 'avg_humidity', 'avg_wind', 'rainfall'
]

# Step 2: Convert 'date' to datetime
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Step 3: Feature Engineering
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Step 4: Handle missing values
df = df.dropna()  # or fillna if you'd like

# Step 5: Save cleaned data
df.to_csv('cleaned_sales_data.csv', index=False)
print("✅ Cleaned data saved as 'cleaned_sales_data.csv'")
