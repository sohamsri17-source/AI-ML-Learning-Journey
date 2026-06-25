import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', np.nan, 'David', 'Eva'],
    'Math_Score': [78, np.nan, 92, 64, 80],
    'Science_Score': [82, 79, 89, np.nan, 90]
}

df = pd.DataFrame(data)

# Detecting and counting missing values per column
summary = df.isnull().sum()
print("Summary of missing values per column:")
print(summary)

# Dropping missing values from specific column
df = df.dropna(subset=['Name'])

# Replace NaN values in Math and Science with their respective column averages
df['Math_Score'] = df['Math_Score'].fillna(df['Math_Score'].mean())
df['Science_Score'] = df['Science_Score'].fillna(df['Science_Score'].mean())

print("\nCleaned DataFrame:")
print(df)