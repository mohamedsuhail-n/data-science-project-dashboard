import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv('cleaned_sales_data.csv')

# Create SQLite engine (DB will be created if it doesn't exist)
engine = create_engine('sqlite:///sales_data.db', echo=False)

# Load data into SQLite table named 'sales'
df.to_sql('sales', con=engine, if_exists='replace', index=False)

print("✅ Data loaded into SQLite DB (sales_data.db) under table 'sales'")
