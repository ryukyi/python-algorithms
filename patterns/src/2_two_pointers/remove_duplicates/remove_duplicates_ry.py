# # Remove Duplicates (easy) ✩

# Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space; 

# after removing the duplicates in-place return the length of the subarray that has no duplicate in it.


# ### Example 1
# ```
# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
# ```

# ### Example 2
# ```
# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].
# ```


def remove_duplicates(arr):
    distinct = set()
    unique_idx = 0
    i = 0
    while i < len(arr):
        if arr[i] not in distinct:
            distinct.add(arr[i])
            arr[unique_idx], arr[i] = arr[i], arr[unique_idx]
            unique_idx += 1
            i += 1
        else:
            i += 1
    return unique_idx
            


        

