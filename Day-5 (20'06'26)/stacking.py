import numpy as np

array_A = np.array([1,2,3])
array_B = np.array([4,5,6])

print(np.vstack((array_A, array_B)))
print("-"*30)
print(np.hstack((array_A, array_B)))