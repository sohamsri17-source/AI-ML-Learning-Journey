import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Math_Score': [78, 85, 92, 64],
    'Science_Score': [82, 79, 89, 70]
}

# Construct the DataFrame
df = pd.DataFrame(data)

# Prints the entire DataFrame
print(df)
print(df.describe())

"""Output:-

      Name  Math_Score  Science_Score
0    Alice          78             82
1      Bob          85             79
2  Charlie          92             89
3    David          64             70 

"""