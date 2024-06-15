""" 
# Maximum Sum Subarray of Size K (easy) ✩

Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.


### Example 1
Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

### Example 2
Input: [2, 3, 4, 1, 5], k=2 
Output: 7
Explanation: Subarray with maximum sum is [3, 4].
"""

# Attempt1:

def max_sum_subarray(arr, k):
    left, max_sum = 0, 0
    for right in range(k, len(arr)):
        window = arr[left:right]
        curr_sum = sum(window)
        if curr_sum > max_sum:
            max_sum = curr_sum
            print(f"Current sum: {curr_sum}")
            print(window)
        left += 1
    return max_sum


result1 = max_sum_subarray([2, 1, 5, 1, 3, 2], 3)
print("Maximum sum of subarrays of size K: " + str(result1) + "\n\n")


result2 = max_sum_subarray([2, 3, 4, 1, 5], 2)
print("Maximum sum of subarrays of size K: " + str(result2) + "\n\n")