import numpy as np

# Create a 1D array of 10 random integers between 10 and 50
random_array = np.random.randint(low=10, high=51, size=10)

print("Original Random Array:")
print(random_array)

# Filter the array to get values greater than 30
filtered_values = random_array[random_array > 30]

print("Boolean Mask (array > 30):")
print(random_array > 30)

print("Values greater than 30:")
print(filtered_values)

""" Output:-

Original Random Array:
[44 45 45 10 21 23 36 16 43 11]

Boolean Mask (array > 30):
[ True  True  True False False False  True False  True False]

Values greater than 30:
[44 45 45 36 43] """
