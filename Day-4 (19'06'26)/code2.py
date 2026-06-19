import numpy as np

# Create a 2x3 matrix with numbers 1 through 6
matrix1 = np.arange(1, 7).reshape(2, 3)
print("Original 2x3 Matrix:")
print(matrix1)

# Multiply the entire matrix by 5 (Scalar broadcasting)
matrix2 = matrix1 * 5
print("After Scalar Multiplication by 5:")
print(matrix2)

# Create a second 2x3 matrix of all ones and add it
matrix3 = np.ones((2, 3), dtype=int)  # dtype=int keeps it matching the original array type
final_matrix = matrix2 + matrix3

print("Matrix of All Ones:")
print(matrix3)
print("Final Result (Multiplied Matrix + Ones Matrix):")
print(final_matrix)
