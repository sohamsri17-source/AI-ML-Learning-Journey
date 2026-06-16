# Finding the second largest element in an array 
# By using built in functions of python
# Time complexity : O(n) + O(n) ≈ O(n)

arr = [12, 9, 10, 27, 25, 30, 2]
largest = max(arr)
sec_largest = -1
for i in range(0, len(arr)):
    if arr[i] > sec_largest and arr[i] != largest:
        sec_largest = arr[i]

print("Second largest is:", sec_largest)  
