# ufunc - stands for universal functions and they are actually numpy functions that operates on the ndarray object.
# ufunc also takes additional arguements like, where, dtype and out.
# Vectorisation - converting iterative based statements into a vector based statement 

# without ufunc :-
x = [1,2,3,4,5]
y = [6,7,8,9,10]
z = []
for i, j in zip(x,y):
    z.append(i+j)
print(z)

# with ufunc :-
import numpy as np

x = [1,2,3,4,5]
y = [6,7,8,9,10]
z = np.add(x,y)
print(z)
