import numpy as np

# Recreating the matrix from the previous step
matrix = np.arange(10, 22).reshape(3, 4)

# Flatten the matrix
flat_array = matrix.flatten()

print("Flattened Array:")
print(flat_array)