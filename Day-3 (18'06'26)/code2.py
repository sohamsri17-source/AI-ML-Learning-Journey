import numpy as np

# Create the 1D array with 12 elements (from 10 to 21)
arr = np.arange(10, 22)

# Reshape into a 3 x 4 matrix (3 rows, 4 columns)
matrix = arr.reshape(3, 4)
print("Reshaped Matrix:")
print(matrix)

# 1. Extract the first row
first_row = matrix[0, :]
print("First Row:")
print(first_row)

# 2. Extract the last two columns
last_two_cols = matrix[:, -2:]
print("Last Two Columns:")
print(last_two_cols)