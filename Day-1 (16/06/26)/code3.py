# Reversing an array using two pointers technique
# Time Complexity : O(n)

def reverse_arr(arr):
    l = 0               # Left pionter
    r = len(arr)-1      # Right pointer
    while l <= r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    return arr 

arr = [12, 9, 10, 27, 25, 30, 2]
print(reverse_arr(arr))
