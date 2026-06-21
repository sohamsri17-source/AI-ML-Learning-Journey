import numpy as np

# Create a 2D array with 4 rows and 2 columns
matrix_1 = np.arange(1, 9).reshape(4, 2)

print(matrix_1)
print("-"*30)
print(np.vsplit(matrix_1, 2))

"""Output:-
 """