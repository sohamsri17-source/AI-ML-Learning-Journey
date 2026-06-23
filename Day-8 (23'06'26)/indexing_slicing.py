import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Math_Score': [78, 85, 92, 64],
    'Science_Score': [82, 79, 89, 70]
}

df = pd.DataFrame(data)

# Selecting and printing specific columns
selected_columns = df[['Name', 'Science_Score']]
print(selected_columns)

# Selecting and printing the 3rd row
charlie_row = df.iloc[2]
print(charlie_row)