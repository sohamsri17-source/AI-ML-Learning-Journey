import numpy as np

# Create a 2D array with 4 rows and 2 columns
matrix_1 = np.arange(1, 9).reshape(4, 2)

print(matrix_1)
print("-"*30)
print(np.vsplit(matrix_1, 2))

""" Output:-
 [[1 2]
 [3 4]
 [5 6]
 [7 8]]
------------------------------
[array([[1, 2],
        [3, 4]]), 

array([[5, 6],
       [7, 8]])]

​ML Application: This is exactly how datasets are split vertically into a training set and a validation set.
"""
