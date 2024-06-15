# # Squaring a Sorted Array (easy) ✩

# Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

# ### Example 1
# ```
# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
# ```

# ### Example 2
# ```
# Input: [-3, -1, 0, 1, 2]
# Output: [0, 1, 1, 4, 9]
# ```

def square_sorted_array(arr):
    result = []
    previous_square, previous_idx = 0, 0
    for right in range(len(arr)):
        square = arr[right] * arr[right]
        if square > previous_square:
            result.insert(previous_idx+1, square)
        else:
            result.insert(previous_idx, square)
    return result