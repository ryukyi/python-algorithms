# # Remove Keys (easy) ✩

# Given an unsorted array of numbers and a target ‘key’, 
# remove all instances of ‘key’ in-place and return the new length of the array.

# ### Example 1
# Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
# Output: 4
# Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

# ### Example 2
# Input: [2, 11, 2, 2, 1], Key=2
# Output: 2
# Explanation: The first two elements after removing every 'Key' will be [11, 1].

def remove_key(arr, k):
    left, right = 0, 0
    while right < len(arr):
        if arr[left] == k and arr[right] == k:
            right += 1
        elif arr[left] == k and arr[right] != k:
            arr[left], arr[right] = arr[right], arr[left]
            right += 1
            left += 1
        else:
            right += 1
    return left
        

