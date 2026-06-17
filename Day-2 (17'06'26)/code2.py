import numpy as np

array  = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9]])

print(array.ndim)  # tells about the axis, axis = 0 (x-axis) is column and axis = 1 (y-axis)
print(array.shape)  # Output = (3,3)

column_sum = np.sum(array, axis=0)
row_sum = np.sum(array,  axis=1)

print("Original Array:\n", array)
print("Transposed Array:\n", array.T)
print("Sum of each column:", column_sum)  # Output: [12 15 18]
print("Sum of each row:", row_sum)        # Output: [ 6 15 24]
