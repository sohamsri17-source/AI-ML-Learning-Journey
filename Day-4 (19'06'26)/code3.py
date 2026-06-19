import numpy as np

# Final matrix from code2
final_matrix = np.array([[ 6, 11, 16],
                         [21, 26, 31]])

# Find the global maximum value
global_max = np.max(final_matrix)

# Sum of each column (axis=0)
column_sums = np.sum(final_matrix, axis=0)

# Mean of each row (axis=1)
row_means = np.mean(final_matrix, axis=1)

# Display Results
print("Final Matrix:", final_matrix)

print(f"Global Maximum Value: {global_max}")

print(f"Sum of each column (axis=0): {column_sums}")

print(f"Mean of each row (axis=1): {row_means}")

"""Output :  """