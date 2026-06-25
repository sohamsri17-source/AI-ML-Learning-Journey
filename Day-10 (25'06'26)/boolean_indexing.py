import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', np.nan, 'David', 'Eva'],
    'Math_Score': [78, np.nan, 92, 64, 80],
    'Science_Score': [82, 79, 89, np.nan, 90]
}

df = pd.DataFrame(data)

# Cleaning Entire DataFrame
df = df.dropna(subset=['Name'])
df['Math_Score'] = df['Math_Score'].fillna(df['Math_Score'].mean())
df['Science_Score'] = df['Science_Score'].fillna(df['Science_Score'].mean())
print("\nCleaned DataFrame:")
print(df)

# Boolean Indexing for Math > 85 AND Science > 85
high_achievers = df[(df['Math_Score'] > 85) & (df['Science_Score'] > 85)]

print("High Achievers (Scored > 85 in both subjects):")
print(high_achievers)

""" 
Output :-
Cleaned DataFrame:
    Name  Math_Score  Science_Score
0  Alice        78.0      82.000000
1    Bob        74.0      79.000000
3  David        64.0      83.666667
4    Eva        80.0      90.000000
High Achievers (Scored > 85 in both subjects):
Empty DataFrame
Columns: [Name, Math_Score, Science_Score]
Index: []
"""
