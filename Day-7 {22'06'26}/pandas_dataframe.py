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

count    4.000000       4.000000
mean    79.750000      80.000000
std     11.954776       7.874008
min     64.000000      70.000000
25%     74.500000      76.750000
50%     81.500000      80.500000
75%     86.750000      83.750000
max     92.000000      89.000000

Pandas instantly calculates the mean, median (50%), min, max, and standard deviation 
for both columns simultaneously without needing individual NumPy functions.

"""
