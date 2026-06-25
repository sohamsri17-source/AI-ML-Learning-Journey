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

"""Output :-
Summary of missing values per column:
Name             1
Math_Score       1
Science_Score    1
dtype: int64

Cleaned DataFrame:
    Name  Math_Score  Science_Score
0  Alice        78.0      82.000000
1    Bob        74.0      79.000000
3  David        64.0      83.666667
4    Eva        80.0      90.000000
"""
