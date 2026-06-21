import numpy as np 

marks = np.array([78,85,92,64,89,75,81,95])

print(np.mean(marks))
print(np.median(marks))
print(np.std(marks))

print(f"The top student is at index {np.argmax(marks)}, with the score of {np.max(marks)}.")

"""Output:- 
82.375
83.0
9.45961812125627
The top student is at index 7, wit the score of 95.
"""
